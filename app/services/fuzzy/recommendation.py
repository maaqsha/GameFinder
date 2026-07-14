import mysql.connector
import re
from .fuzzification import fuzzify_game
from .inference import generate_rules, evaluate_rules
from .aggregation import aggregate
from .defuzzification import centroid

_RULES = None
_DB_CONFIG = None

MIN_REVIEWS = 5

CONTENT_BLOCK_PATTERNS = [
    r'\bsexual content\b',
    r'\bnudity\b',
    r'\bhentai\b',
    r'\bnsfw\b',
    r'\bporn(ographic)?\b',
    r'\berotic\b',
    r'\badult\b',
]

_CONTENT_RE = None


def _get_content_re():
    global _CONTENT_RE
    if _CONTENT_RE is None:
        pattern = '|'.join(CONTENT_BLOCK_PATTERNS)
        _CONTENT_RE = re.compile(pattern, re.IGNORECASE)
    return _CONTENT_RE


def _is_content_blocked(genre, tags, name=None):
    cr = _get_content_re()
    if genre and cr.search(genre):
        return True
    if tags and cr.search(tags):
        return True
    if name:
        name_lower = name.lower()
        for kw in ['hentai', 'nsfw', 'sex ', ' sex', 'porn', 'erotic']:
            if kw in name_lower:
                return True
    return False


def _get_rules():
    global _RULES
    if _RULES is None:
        _RULES = generate_rules()
    return _RULES


def _get_db():
    global _DB_CONFIG
    if _DB_CONFIG is None:
        _DB_CONFIG = {
            'host': 'localhost',
            'user': 'root',
            'password': '',
            'database': 'gamefinder',
        }
    return mysql.connector.connect(**_DB_CONFIG)


def evaluate_game(price_idr, pc_level, rating_percentage, playtime_hours,
                  preferred_rating=100, preferred_playtime=50,
                  preferred_gamer_type=2):
    fuzzy_inputs = fuzzify_game(price_idr, pc_level, rating_percentage, playtime_hours,
                                preferred_rating, preferred_playtime,
                                preferred_gamer_type)
    rules = _get_rules()
    strengths = evaluate_rules(fuzzy_inputs, rules)
    agg = aggregate(strengths)
    score = centroid(agg)
    return round(score, 2), agg


def score_category(score):
    if score <= 25:
        return 'Not Recommended'
    if score <= 50:
        return 'Less Recommended'
    if score <= 75:
        return 'Recommended'
    return 'Highly Recommended'


GAMER_NAMES = {1: 'Casual', 2: 'Balanced', 3: 'Hardcore'}


PC_NAMES = {1: 'Low End', 2: 'Mid End', 3: 'High End'}


def _build_reasons(game, budget, pc_level, preferred_rating, preferred_playtime,
                   preferred_gamer_type=2):
    reasons = []
    total_reviews = int(game['total_reviews'])
    estimated_owners = int(game.get('estimated_owners', 0))
    peak_players = int(game.get('peak_players', 0))

    gamer_label = GAMER_NAMES.get(preferred_gamer_type, 'Balanced')
    reasons.append({'key': 'gamer_type', 'text': f'Matched for {gamer_label} play style', 'match': 'excellent'})

    pc_label = PC_NAMES.get(pc_level, 'Mid End')
    reasons.append({'key': 'pc_level', 'text': f'PC level {pc_label} — performance matched to your system', 'match': 'excellent'})

    price = float(game['price_idr'])
    if price <= budget:
        if price == 0:
            reasons.append({'key': 'budget', 'text': 'Free game — fits any budget', 'match': 'excellent'})
        else:
            reasons.append({'key': 'budget', 'text': f'Rp {price:,.0f} is within your Rp {budget:,.0f} budget', 'match': 'excellent'})
    else:
        reasons.append({'key': 'budget', 'text': f'Rp {price:,.0f} exceeds your Rp {budget:,.0f} budget', 'match': 'poor'})

    rating = float(game['rating_percentage'])
    if rating >= preferred_rating:
        reasons.append({'key': 'rating', 'text': f'Rating {rating:.0f}% meets your {preferred_rating:.0f}% preference', 'match': 'excellent'})
    elif rating >= preferred_rating * 0.7:
        reasons.append({'key': 'rating', 'text': f'Rating {rating:.0f}% is close to your {preferred_rating:.0f}% preference', 'match': 'good'})
    else:
        reasons.append({'key': 'rating', 'text': f'Rating {rating:.0f}% is below your {preferred_rating:.0f}% preference', 'match': 'poor'})

    if estimated_owners >= 1000000:
        reasons.append({'key': 'community', 'text': f'{estimated_owners:,} estimated owners — massive player base', 'match': 'excellent'})
    elif estimated_owners >= 100000:
        reasons.append({'key': 'community', 'text': f'{estimated_owners:,} estimated owners — large community', 'match': 'good'})
    elif peak_players >= 1000:
        reasons.append({'key': 'community', 'text': f'{peak_players:,} peak players — active community', 'match': 'good'})
    elif total_reviews >= 50:
        reasons.append({'key': 'community', 'text': f'{total_reviews} reviews — trusted by the community', 'match': 'excellent'})
    elif total_reviews >= MIN_REVIEWS:
        reasons.append({'key': 'community', 'text': f'{total_reviews} reviews — some community feedback', 'match': 'good'})

    if total_reviews >= 20 and rating >= 80:
        reasons.append({'key': 'popular', 'text': f'{rating:.0f}% positive from {total_reviews:,} reviews', 'match': 'excellent'})

    return reasons


def recommend(budget, pc_level, preferred_rating, preferred_playtime, genre,
              top_n=10, preferred_gamer_type=2):
    conn = _get_db()
    cursor = conn.cursor(dictionary=True)

    genres = [g.strip() for g in genre.split(',') if g.strip()]

    def build_genre_where(genres):
        if not genres:
            return None, []
        clauses = []
        params = []
        for g in genres:
            clauses.append(
                "(genre LIKE CONCAT('%', %s, '%') OR tags LIKE CONCAT('%', %s, '%'))"
            )
            params.append(g)
            params.append(g)
        return ' AND '.join(clauses), params

    genre_clause, genre_params = build_genre_where(genres)

    select_cols = """
        SELECT app_id, name, price_idr, rating_percentage,
               total_reviews, genre, tags,
               estimated_owners, peak_players
        FROM games
    """

    candidates = []
    where_parts = ["total_reviews >= %s"]
    where_params = [MIN_REVIEWS]

    if genre_clause:
        where_parts.append(genre_clause)
        where_params.extend(genre_params)

    # Coba dengan anggaran pengguna terlebih dahulu
    where_parts_budget = where_parts + ["price_idr <= %s"]
    sql = select_cols + " WHERE " + " AND ".join(where_parts_budget)
    cursor.execute(sql, where_params + [budget])
    candidates = cursor.fetchall()

    # Jika tidak ada hasil dengan anggaran, coba lagi dengan anggaran maksimum
    if not candidates:
        sql = select_cols + " WHERE " + " AND ".join(where_parts)
        cursor.execute(sql, where_params)
        candidates = cursor.fetchall()

    cursor.close()
    conn.close()

    results = []
    for g in candidates:
        if _is_content_blocked(g['genre'], g['tags'], g['name']):
            continue

        score, _ = evaluate_game(
            price_idr=float(g['price_idr']),
            pc_level=pc_level,
            rating_percentage=float(g['rating_percentage']),
            playtime_hours=preferred_playtime,
            preferred_rating=preferred_rating,
            preferred_playtime=preferred_playtime,
            preferred_gamer_type=preferred_gamer_type,
        )
        cat = score_category(score)
        reasons = _build_reasons(g, budget, pc_level, preferred_rating,
                                 preferred_playtime, preferred_gamer_type)
        release_year = None
        if g.get('release_date'):
            try:
                release_year = int(str(g['release_date'])[:4])
            except (ValueError, TypeError):
                pass

        results.append({
            'app_id': g['app_id'],
            'name': g['name'],
            'price_idr': g['price_idr'],
            'rating_percentage': g['rating_percentage'],
            'genre': g['genre'],
            'tags': g['tags'],
            'total_reviews': g['total_reviews'],
            'estimated_owners': g['estimated_owners'],
            'peak_players': g['peak_players'],
            'release_year': release_year,
            'recommendation_score': score,
            'recommendation_category': cat,
            'reasons': reasons,
        })

    results.sort(key=lambda x: (x['recommendation_score'], x['estimated_owners']), reverse=True)
    return results[:top_n]


def demo():
    print('Recommendation Engine Demo')
    print('=' * 60)
    print()
    print('User Profile:')
    print('  Budget: 300,000 IDR')
    print('  PC Level: 2 (Medium)')
    print('  Gamer Type: 2 (Balanced)')
    print('  Preferred Rating: 75%')
    print('  Preferred Playtime: 20 hours')
    print('  Genre: Action')
    print()

    results = recommend(
        budget=300000,
        pc_level=2,
        preferred_rating=75,
        preferred_playtime=20,
        genre='Action',
        top_n=10,
        preferred_gamer_type=2,
    )

    if not results:
        print('No matching games found.')
        return

    header = f'{"#":<3} {"Name":<40} {"Price(IDR)":<12} {"Rating":<8} {"Genre":<20} {"Score":<8} {"Category":<20} {"Owners":<12}'
    print(header)
    print('-' * 120)
    for i, g in enumerate(results, 1):
        name = g['name'][:38]
        price = f'{int(g["price_idr"]):>10,}'
        rating = f'{g["rating_percentage"]:>6.2f}%'
        print(f'{i:<3} {name:<40} Rp{price:<9} {rating:<8} {g["genre"]:<20} {g["recommendation_score"]:<8} {g["recommendation_category"]:<20} {g["estimated_owners"]:>10,}')


if __name__ == '__main__':
    demo()
