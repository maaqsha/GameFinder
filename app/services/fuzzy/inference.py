OUTPUT_CATEGORIES = ['Not Recommended', 'Less Recommended', 'Recommended', 'Highly Recommended']

LABELS = {
    'budget': ['Low', 'Medium', 'High'],
    'pc_level': ['Low', 'Medium', 'High'],
    'rating': ['Low', 'Medium', 'High'],
    'playtime': ['Short', 'Medium', 'Long'],
}


def _is_good(var, label):
    if var == 'pc_level':
        return label == 'Low'
    if var == 'rating':
        return label == 'High'
    if var == 'budget':
        return label == 'Low'
    if var == 'playtime':
        return label == 'Medium'
    return False


def _is_bad(var, label):
    if var == 'pc_level':
        return label == 'High'
    if var == 'rating':
        return label == 'Low'
    if var == 'budget':
        return label == 'High'
    if var == 'playtime':
        return label == 'Short' or label == 'Long'
    return False


def _get_output(budget, pc, rating, playtime):
    pc_bad = _is_bad('pc_level', pc)
    pc_good = _is_good('pc_level', pc)
    rating_bad = _is_bad('rating', rating)
    rating_good = _is_good('rating', rating)
    budget_bad = _is_bad('budget', budget)
    budget_good = _is_good('budget', budget)
    playtime_bad = _is_bad('playtime', playtime)
    playtime_good = _is_good('playtime', playtime)

    goods = sum([pc_good, rating_good, budget_good, playtime_good])
    bads = sum([pc_bad, rating_bad, budget_bad, playtime_bad])

    if pc_bad and (rating_bad or budget_bad):
        return 0

    if pc_bad and rating_good and not budget_bad and not playtime_bad:
        return 1

    if pc_bad:
        return 0

    if rating_bad and not pc_good and budget_bad:
        return 0

    if goods >= 3 and not rating_bad:
        return 3

    if pc_good and rating_good and not budget_bad and not playtime_bad:
        return 3

    if pc_good and rating_good:
        return 2

    if goods >= 3:
        return 1

    if goods >= 2 and bads == 0:
        return 2

    if goods >= 1 and bads <= 1:
        return 1

    if bads == 0:
        return 1

    return 0


def generate_rules():
    rules = []
    for b in LABELS['budget']:
        for p in LABELS['pc_level']:
            for r in LABELS['rating']:
                for pt in LABELS['playtime']:
                    idx = _get_output(b, p, r, pt)
                    rules.append({
                        'antecedent': {'budget': b, 'pc_level': p, 'rating': r, 'playtime': pt},
                        'consequent': OUTPUT_CATEGORIES[idx],
                    })
    return rules


def evaluate_rules(fuzzy_inputs, rules):
    strengths = {cat: 0.0 for cat in OUTPUT_CATEGORIES}
    for rule in rules:
        ant = rule['antecedent']
        firing = min(
            fuzzy_inputs['budget'][ant['budget']],
            fuzzy_inputs['pc_level'][ant['pc_level']],
            fuzzy_inputs['rating'][ant['rating']],
            fuzzy_inputs['playtime'][ant['playtime']],
        )
        if firing > strengths[rule['consequent']]:
            strengths[rule['consequent']] = firing
    return strengths
