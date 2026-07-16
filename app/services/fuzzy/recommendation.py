import mysql.connector
import re
from .fuzzification import fuzzify_game
from .inference import generate_rules, evaluate_rules
from .aggregation import aggregate
from .defuzzification import centroid
from app.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

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
            'host': MYSQL_HOST,
            'user': MYSQL_USER,
            'password': MYSQL_PASSWORD,
            'database': MYSQL_DATABASE,
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
    return round(score, 2), agg, fuzzy_inputs


def score_category(score):
    if score <= 25:
        return 'Not Recommended'
    if score <= 50:
        return 'Less Recommended'
    if score <= 75:
        return 'Recommended'
    return 'Highly Recommended'


GAMER_NAMES = {1: 'Kasual', 2: 'Seimbang', 3: 'Hardcore'}


PC_NAMES = {1: 'Low End', 2: 'Mid End', 3: 'High End'}


def _estimate_game_features(game):
    tags = (game.get('tags') or '').lower()
    genre = (game.get('genre') or '').lower()
    
    # Estimasi PC Level
    pc_level = 2
    if any(t in tags for t in ['pixel graphics', '2d', 'retro', 'minimalist', 'visual novel', 'text-based', 'point & click', 'platformer']):
        pc_level = 1
    if any(t in tags for t in ['realistic', 'open world', 'vr', 'ray tracing', 'cyberpunk', 'next gen', 'simulation', 'survival']):
        pc_level = 3
        
    # Estimasi Playtime
    playtime_hours = 30
    if any(t in tags for t in ['rpg', 'mmo', 'massively multiplayer', 'strategy', 'open world', 'survival']):
        playtime_hours = 80
    elif any(t in tags for t in ['casual', 'puzzle', 'short', 'platformer', 'visual novel', 'indie']):
        playtime_hours = 12
    
    # Variasi kecil berdasarkan app_id agar tidak seragam persis
    variance = (game.get('app_id', 0) % 15) - 7
    playtime_hours = max(2, playtime_hours + variance)
    
    return pc_level, playtime_hours


def _build_reasons(game, budget, user_pc_level, preferred_rating, preferred_playtime,
                   preferred_gamer_type=2, game_pc_level=None, game_playtime=None,
                   fuzzy_inputs=None, selected_genre=None):
    if game_pc_level is None or game_playtime is None:
        game_pc_level, game_playtime = _estimate_game_features(game)

    gamer_label = GAMER_NAMES.get(preferred_gamer_type, 'Seimbang')

    def _match(score):
        if score >= 0.8:
            return 'excellent'
        elif score >= 0.5:
            return 'good'
        elif score >= 0.2:
            return 'neutral'
        return 'poor'

    reasons = []

    # 1. Budget — bandingkan harga game vs anggaran user
    price = float(game['price_idr'])
    if price == 0:
        reasons.append({'key': 'budget', 'text': 'Gratis — pas dengan semua anggaran', 'match': 'excellent', 'score': 1.0})
    elif price <= budget:
        reasons.append({'key': 'budget', 'text': f'Rp {price:,.0f} — sesuai anggaran Rp {budget:,.0f} Anda', 'match': 'excellent', 'score': 1.0})
    else:
        reasons.append({'key': 'budget', 'text': f'Rp {price:,.0f} — melebihi anggaran Rp {budget:,.0f} Anda', 'match': 'poor', 'score': 0.0})

    # 2. PC Level — bandingkan kebutuhan game vs kemampuan PC user
    game_pc_label = PC_NAMES.get(game_pc_level, 'Mid End')
    user_pc_label = PC_NAMES.get(user_pc_level, 'Mid End')
    if game_pc_level <= user_pc_level:
        reasons.append({'key': 'pc_level', 'text': f'{game_pc_label} — PC Anda mencukupi untuk game ini', 'match': 'excellent', 'score': 1.0})
    else:
        reasons.append({'key': 'pc_level', 'text': f'{game_pc_label} — PC Anda belum mencukupi (butuh {game_pc_label})', 'match': 'poor', 'score': 0.0})

    # 3. Rating — bandingkan rating game vs preferensi rating user
    rating = float(game['rating_percentage'])
    if rating >= preferred_rating:
        reasons.append({'key': 'rating', 'text': f'{rating:.0f}% — memenuhi preferensi {preferred_rating:.0f}% Anda', 'match': 'excellent', 'score': 1.0})
    elif preferred_rating > 0:
        rating_score = min(rating / preferred_rating, 1.0)
        if rating_score >= 0.8:
            reasons.append({'key': 'rating', 'text': f'{rating:.0f}% — mendekati preferensi {preferred_rating:.0f}% Anda', 'match': 'good', 'score': rating_score})
        else:
            reasons.append({'key': 'rating', 'text': f'{rating:.0f}% — belum memenuhi preferensi {preferred_rating:.0f}% Anda', 'match': _match(rating_score), 'score': rating_score})
    else:
        reasons.append({'key': 'rating', 'text': 'Rating tidak dinilai', 'match': 'neutral', 'score': 0.5})

    # 4. Playtime — bandingkan playtime game vs preferensi playtime user
    diff = abs(game_playtime - preferred_playtime)
    if preferred_playtime > 0:
        play_score = max(0, 1.0 - diff / preferred_playtime)
    else:
        play_score = 0.0

    if play_score >= 0.8:
        reasons.append({'key': 'playtime', 'text': f'~{game_playtime:.0f} jam — sesuai preferensi {preferred_playtime:.0f} jam Anda', 'match': 'excellent', 'score': play_score})
    elif game_playtime > preferred_playtime:
        reasons.append({'key': 'playtime', 'text': f'~{game_playtime:.0f} jam — lebih panjang dari preferensi {preferred_playtime:.0f} jam Anda', 'match': _match(play_score), 'score': play_score})
    elif game_playtime < preferred_playtime:
        reasons.append({'key': 'playtime', 'text': f'~{game_playtime:.0f} jam — lebih pendek dari preferensi {preferred_playtime:.0f} jam Anda', 'match': _match(play_score), 'score': play_score})
    else:
        reasons.append({'key': 'playtime', 'text': f'~{game_playtime:.0f} jam', 'match': 'neutral', 'score': play_score})

    # 5. Genre — bandingkan genre game vs genre yang dipilih user
    game_genres = [g.strip().lower() for g in game.get('genre', '').split(',') if g.strip()]
    game_tags = [t.strip().lower() for t in game.get('tags', '').split(',') if t.strip()]
    if selected_genre:
        user_genres = [g.strip().lower() for g in selected_genre.split(',') if g.strip()]
        genre_match = any(ug in game_genres or any(gg.startswith(ug) or ug.startswith(gg) for gg in game_genres) or ug in game_tags for ug in user_genres)
        if genre_match:
            reasons.append({'key': 'genre', 'text': f'{game.get("genre", "")} — sesuai pilihan Anda', 'match': 'excellent', 'score': 1.0})
        else:
            reasons.append({'key': 'genre', 'text': f'{game.get("genre", "")} — berbeda dari pilihan Anda', 'match': 'neutral', 'score': 0.3})
    else:
        reasons.append({'key': 'genre', 'text': f'{game.get("genre", "")}', 'match': 'neutral', 'score': 0.5})

    # 6. Gamer Type — profil gamer yang dipilih user
    reasons.append({'key': 'gamer_type', 'text': f'Profil {gamer_label}', 'match': 'excellent', 'score': 1.0})

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

        game_pc_level, game_playtime = _estimate_game_features(g)

        score, agg, fuzzy_inputs = evaluate_game(
            price_idr=float(g['price_idr']),
            pc_level=game_pc_level,
            rating_percentage=float(g['rating_percentage']),
            playtime_hours=game_playtime,
            preferred_rating=preferred_rating,
            preferred_playtime=preferred_playtime,
            preferred_gamer_type=preferred_gamer_type,
        )
        cat = score_category(score)
        reasons = _build_reasons(g, budget, pc_level, preferred_rating,
                                 preferred_playtime, preferred_gamer_type,
                                 game_pc_level, game_playtime,
                                 fuzzy_inputs=fuzzy_inputs,
                                 selected_genre=genre)

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
