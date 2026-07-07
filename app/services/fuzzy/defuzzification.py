from .aggregation import OUTPUT_MFS


SAMPLES = 1000


def centroid(aggregated_strengths):
    step = 100.0 / SAMPLES
    numerator = 0.0
    denominator = 0.0
    for i in range(SAMPLES + 1):
        x = i * step
        mu = 0.0
        for cat, strength in aggregated_strengths.items():
            mf = OUTPUT_MFS[cat]
            clipped = min(mf(x), strength)
            if clipped > mu:
                mu = clipped
        numerator += mu * x
        denominator += mu
    return numerator / denominator if denominator > 0 else 0.0
