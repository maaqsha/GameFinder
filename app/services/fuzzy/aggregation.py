from .membership import REC_NOT, REC_LESS, REC_YES, REC_HIGH

OUTPUT_MFS = {
    'Not Recommended': REC_NOT,
    'Less Recommended': REC_LESS,
    'Recommended': REC_YES,
    'Highly Recommended': REC_HIGH,
}


def aggregate(rule_strengths):
    return {
        cat: rule_strengths.get(cat, 0.0)
        for cat in OUTPUT_MFS
    }
