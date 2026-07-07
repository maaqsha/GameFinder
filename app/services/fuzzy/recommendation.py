import mysql.connector
from .fuzzification import fuzzify_game
from .inference import generate_rules, evaluate_rules
from .aggregation import aggregate
from .defuzzification import centroid

_RULES = None
_DB_CONFIG = None


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


def recommend(budget, pc_level, preferred_rating, preferred_playtime, genre, top_n=10):
    conn = _get_db()
    cursor = conn.cursor(dictionary=True)

    # Evaluate top candidates by rating — lower-rated games won't rank in Top 10
    sql = """
        SELECT app_id, name, price_idr, positive, negative,
               rating_percentage, playtime_hours,
               genre, pc_level, header_image, short_description
        FROM games
        WHERE MATCH(genre) AGAINST(%s IN BOOLEAN MODE)
          AND pc_level <= %s
          AND price_idr <= %s
        ORDER BY rating_percentage DESC
        LIMIT 200
    """
    cursor.execute(sql, (genre, pc_level, budget))
    candidates = cursor.fetchall()
    cursor.close()
    conn.close()

    results = []
    for g in candidates:
        score, _ = evaluate_game(
            price_idr=float(g['price_idr']),
            pc_level=int(g['pc_level']),
            rating_percentage=float(g['rating_percentage']),
            playtime_hours=float(g['playtime_hours']),
            preferred_rating=preferred_rating,
            preferred_playtime=preferred_playtime,
        )
        cat = score_category(score)
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
            'recommendation_score': score,
            'recommendation_category': cat,
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
