from .membership import (
    BUDGET_LOW, BUDGET_MEDIUM, BUDGET_HIGH,
    PC_LEVEL_LOW, PC_LEVEL_MEDIUM, PC_LEVEL_HIGH,
    RATING_LOW, RATING_MEDIUM, RATING_HIGH,
    PLAYTIME_SHORT, PLAYTIME_MEDIUM, PLAYTIME_LONG,
)


def fuzzify_budget(price_idr):
    return {
        'Low': BUDGET_LOW(price_idr),
        'Medium': BUDGET_MEDIUM(price_idr),
        'High': BUDGET_HIGH(price_idr),
    }


def fuzzify_pc_level(pc_level):
    return {
        'Low': PC_LEVEL_LOW(pc_level),
        'Medium': PC_LEVEL_MEDIUM(pc_level),
        'High': PC_LEVEL_HIGH(pc_level),
    }


def fuzzify_rating(rating_percentage):
    return {
        'Low': RATING_LOW(rating_percentage),
        'Medium': RATING_MEDIUM(rating_percentage),
        'High': RATING_HIGH(rating_percentage),
    }


def fuzzify_playtime(playtime_hours):
    return {
        'Short': PLAYTIME_SHORT(playtime_hours),
        'Medium': PLAYTIME_MEDIUM(playtime_hours),
        'Long': PLAYTIME_LONG(playtime_hours),
    }


def fuzzify_game(price_idr, pc_level, rating_percentage, playtime_hours):
    return {
        'budget': fuzzify_budget(price_idr),
        'pc_level': fuzzify_pc_level(pc_level),
        'rating': fuzzify_rating(rating_percentage),
        'playtime': fuzzify_playtime(playtime_hours),
    }
