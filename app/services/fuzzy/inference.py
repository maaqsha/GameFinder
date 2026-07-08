OUTPUT_CATEGORIES = ['Not Recommended', 'Less Recommended', 'Recommended', 'Highly Recommended']

LABELS = {
    'budget': ['Low', 'Medium', 'High'],
    'pc_level': ['Low', 'Medium', 'High'],
    'gamer_type': ['Casual', 'Balanced', 'Hardcore'],
    'rating': ['Low', 'Medium', 'High'],
    'playtime': ['Short', 'Medium', 'Long'],
}

GAMER_PROFILES = {
    'Casual': {'budget': 'Low', 'pc_level': 'Low', 'rating': 'Medium', 'playtime': 'Short'},
    'Balanced': {'budget': 'Low', 'pc_level': 'Low', 'rating': 'High', 'playtime': 'Medium'},
    'Hardcore': {'budget': 'High', 'pc_level': 'High', 'rating': 'High', 'playtime': 'Long'},
}


def _get_output(budget, pc, gamer, rating, playtime):
    ideal = GAMER_PROFILES[gamer]
    matches = sum([
        budget == ideal['budget'],
        pc == ideal['pc_level'],
        rating == ideal['rating'],
        playtime == ideal['playtime'],
    ])
    return {4: 3, 3: 2, 2: 1}.get(matches, 0)


def generate_rules():
    rules = []
    for b in LABELS['budget']:
        for p in LABELS['pc_level']:
            for g in LABELS['gamer_type']:
                for r in LABELS['rating']:
                    for pt in LABELS['playtime']:
                        idx = _get_output(b, p, g, r, pt)
                        rules.append({
                            'antecedent': {
                                'budget': b, 'pc_level': p,
                                'gamer_type': g,
                                'rating': r, 'playtime': pt,
                            },
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
            fuzzy_inputs['gamer_type'][ant['gamer_type']],
            fuzzy_inputs['rating'][ant['rating']],
            fuzzy_inputs['playtime'][ant['playtime']],
        )
        if firing > strengths[rule['consequent']]:
            strengths[rule['consequent']] = firing
    return strengths