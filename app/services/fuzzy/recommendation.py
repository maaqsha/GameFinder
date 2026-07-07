import mysql.connector
import re
from .fuzzification import fuzzify_game
from .inference import generate_rules, evaluate_rules
from .aggregation import aggregate
from .defuzzification import centroid

_RULES = None
_DB_CONFIG = None

# --- Quality constants (derived from dataset analysis) ---
GLOBAL_AVG_RATING = 75.19     # average rating_percentage across games with 5+ reviews
BAYESIAN_K = 10                # smoothing factor — lower = less smoothing, higher = more weight on global avg
MIN_REVIEWS = 5                # minimum positive+negative reviews to be considered

# --- Configurable content filter ---
# Games whose genre matches any of these patterns (case-insensitive, regex) are excluded.
# Kept as a simple list for easy maintenance — add/remove patterns as needed.
CONTENT_BLOCK_PATTERNS = [
    r'\bsexual content\b',
    r'\bnudity\b',
    r'\bhentai\b',
    r'\bnsfw\b',
    r'\bporn(ographic)?\b',
    r'\berotic\b',
]

_CONTENT_RE = None


def _get_content_re():
    global _CONTENT_RE
    if _CONTENT_RE is None:
        pattern = '|'.join(CONTENT_BLOCK_PATTERNS)
        _CONTENT_RE = re.compile(pattern, re.IGNORECASE)
    return _CONTENT_RE


def _is_content_blocked(genre):
    if not genre:
        return False
    return bool(_get_content_re().search(genre))


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
                  preferred_rating=100, preferred_playtime=50):
    fuzzy_inputs = fuzzify_game(price_idr, pc_level, rating_percentage, playtime_hours,
                                preferred_rating, preferred_playtime)
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


def _bayesian_score(rating_pct, total_reviews):
    """Bayesian weighted rating — pulls low-review-count games toward the global average."""
    return (GLOBAL_AVG_RATING * BAYESIAN_K + rating_pct * total_reviews) / (BAYESIAN_K + total_reviews)


def _build_reasons(game, budget, pc_level, preferred_rating, preferred_playtime):
    """Build human-readable reasons explaining why this game was recommended."""
    reasons = []
    total_reviews = int(game['positive']) + int(game['negative'])

    # 1. Budget
    if float(game['price_idr']) <= budget:
        if float(game['price_idr']) == 0:
            reasons.append({'key': 'budget', 'text': 'Free game — fits any budget', 'match': 'excellent'})
        else:
            reasons.append({'key': 'budget', 'text': 'Fits your budget', 'match': 'excellent'})
    else:
        reasons.append({'key': 'budget', 'text': 'Exceeds your budget', 'match': 'poor'})

    # 2. PC compatibility
    if int(game['pc_level']) <= pc_level:
        reasons.append({'key': 'pc', 'text': 'Compatible with your PC', 'match': 'excellent'})
    else:
        reasons.append({'key': 'pc', 'text': 'Exceeds your PC specs', 'match': 'poor'})

    # 3. Rating match
    rating = float(game['rating_percentage'])
    if rating >= preferred_rating:
        reasons.append({'key': 'rating', 'text': f'Rating {rating:.0f}% meets your {preferred_rating:.0f}% preference', 'match': 'excellent'})
    elif rating >= preferred_rating * 0.7:
        reasons.append({'key': 'rating', 'text': f'Rating {rating:.0f}% is close to your {preferred_rating:.0f}% preference', 'match': 'good'})
    else:
        reasons.append({'key': 'rating', 'text': f'Rating {rating:.0f}% is below your {preferred_rating:.0f}% preference', 'match': 'poor'})

    # 4. Playtime match
    pt = float(game['playtime_hours'])
    if preferred_playtime > 0:
        ratio = pt / preferred_playtime
        if 0.5 <= ratio <= 2.0:
            reasons.append({'key': 'playtime', 'text': f'Playtime ({pt:.0f}h) matches your preference', 'match': 'excellent'})
        elif ratio < 0.5 and pt > 0:
            reasons.append({'key': 'playtime', 'text': f'Shorter game ({pt:.0f}h) — good for quick sessions', 'match': 'good'})
        elif ratio > 2.0:
            reasons.append({'key': 'playtime', 'text': f'Long game ({pt:.0f}h) — great value for time', 'match': 'good'})
        else:
            reasons.append({'key': 'playtime', 'text': 'Playtime data unavailable', 'match': 'neutral'})
    else:
        reasons.append({'key': 'playtime', 'text': f'Playtime: {pt:.0f}h', 'match': 'neutral'})

    # 5. Community validation
    if total_reviews >= 50:
        reasons.append({'key': 'community', 'text': f'{total_reviews} reviews — trusted by the community', 'match': 'excellent'})
    elif total_reviews >= MIN_REVIEWS:
        reasons.append({'key': 'community', 'text': f'{total_reviews} reviews — some community feedback', 'match': 'good'})

    # 6. Popularity signal
    if total_reviews >= 20 and float(game['rating_percentage']) >= 80:
        reasons.append({'key': 'popular', 'text': 'Highly rated by players', 'match': 'excellent'})

    return reasons


def recommend(budget, pc_level, preferred_rating, preferred_playtime, genre, top_n=10):
    conn = _get_db()
    cursor = conn.cursor(dictionary=True)

    # Candidate selection strategy:
    # 1. Genre + PC + budget pre-filter (existing)
    # 2. MIN_REVIEWS threshold to filter shovelware with no community validation
    # 3. Content filter to block adult/pornographic content
    # 4. Bayesian weighted score ordering — promotes games with many reviews,
    #    demotes games with few reviews but perfect rating
    # 5. LIMIT 200 keeps performance fast
    sql = """
        SELECT app_id, name, price_idr, positive, negative,
               rating_percentage, playtime_hours,
               genre, pc_level, header_image, short_description
        FROM games
        WHERE MATCH(genre) AGAINST(%s IN BOOLEAN MODE)
          AND pc_level <= %s
          AND price_idr <= %s
          AND positive + negative >= %s
        ORDER BY (%s * %s + rating_percentage * (positive + negative)) / (%s + positive + negative) DESC
        LIMIT 200
    """
    cursor.execute(sql, (
        genre,
        pc_level,
        budget,
        MIN_REVIEWS,
        GLOBAL_AVG_RATING, BAYESIAN_K,
        BAYESIAN_K,
    ))
    candidates = cursor.fetchall()
    cursor.close()
    conn.close()

    results = []
    for g in candidates:
        # Skip content-blocked games
        if _is_content_blocked(g['genre']):
            continue

        score, _ = evaluate_game(
            price_idr=float(g['price_idr']),
            pc_level=int(g['pc_level']),
            rating_percentage=float(g['rating_percentage']),
            playtime_hours=float(g['playtime_hours']),
            preferred_rating=preferred_rating,
            preferred_playtime=preferred_playtime,
        )
        cat = score_category(score)
        reasons = _build_reasons(g, budget, pc_level, preferred_rating, preferred_playtime)
        results.append({
            'app_id': g['app_id'],
            'name': g['name'],
            'price_idr': g['price_idr'],
            'rating_percentage': g['rating_percentage'],
            'playtime_hours': g['playtime_hours'],
            'genre': g['genre'],
            'pc_level': g['pc_level'],
            'header_image': g['header_image'],
            'short_description': g['short_description'],
            'positive': g['positive'],
            'negative': g['negative'],
            'recommendation_score': score,
            'recommendation_category': cat,
            'reasons': reasons,
        })

    results.sort(key=lambda x: x['recommendation_score'], reverse=True)
    return results[:top_n]


def demo():
    print('Recommendation Engine Demo')
    print('=' * 60)
    print()
    print('User Profile:')
    print('  Budget: 300,000 IDR')
    print('  PC Level: 2 (Medium)')
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
    )

    if not results:
        print('No matching games found.')
        return

    print(f'Top {len(results)} Recommendations:')
    print('-' * 110)
    header = f'{"#":<3} {"Name":<40} {"Price(IDR)":<12} {"Rating":<8} {"Playtime":<9} {"PC":<4} {"Score":<8} {"Category":<20}'
    print(header)
    print('-' * 110)
    for i, g in enumerate(results, 1):
        name = g['name'][:38]
        price = f'{int(g["price_idr"]):>10,}'
        rating = f'{g["rating_percentage"]:>6.2f}%'
        playtime = f'{g["playtime_hours"]:>7.1f}h'
        print(f'{i:<3} {name:<40} Rp{price:<9} {rating:<8} {playtime:<9} {g["pc_level"]:<4} {g["recommendation_score"]:<8} {g["recommendation_category"]:<20}')


if __name__ == '__main__':
    demo()
