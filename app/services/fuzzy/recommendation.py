from .fuzzification import fuzzify_game
from .inference import generate_rules, evaluate_rules
from .aggregation import aggregate
from .defuzzification import centroid
from .membership import triangular

_RULES = None


def _get_rules():
    global _RULES
    if _RULES is None:
        _RULES = generate_rules()
    return _RULES


def evaluate_game(price_idr, pc_level, rating_percentage, playtime_hours):
    fuzzy_inputs = fuzzify_game(price_idr, pc_level, rating_percentage, playtime_hours)
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


def demo():
    test_cases = [
        {'name': 'Cheap indie (low PC, low price, high rating, short)',
         'price_idr': 50000, 'pc_level': 1, 'rating': 92, 'playtime': 5},
        {'name': 'AAA game (high PC, expensive, high rating, long)',
         'price_idr': 800000, 'pc_level': 3, 'rating': 88, 'playtime': 80},
        {'name': 'Mid-range game (medium PC, medium price, medium rating, medium playtime)',
         'price_idr': 350000, 'pc_level': 2, 'rating': 70, 'playtime': 35},
        {'name': 'Poor game (low rating, expensive, high PC)',
         'price_idr': 950000, 'pc_level': 3, 'rating': 25, 'playtime': 120},
        {'name': 'Budget friendly (low price, medium PC, good rating)',
         'price_idr': 100000, 'pc_level': 2, 'rating': 85, 'playtime': 15},
    ]
    print(f"{'Test Case':<45} {'Score':<8} {'Category':<20}")
    print('-' * 75)
    for tc in test_cases:
        score, _ = evaluate_game(tc['price_idr'], tc['pc_level'], tc['rating'], tc['playtime'])
        cat = score_category(score)
        print(f"{tc['name']:<45} {score:<8} {cat:<20}")


if __name__ == '__main__':
    demo()
