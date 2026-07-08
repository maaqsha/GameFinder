def triangular(x, a, b, c):
    if a == b and x <= a:
        return 1.0
    if b == c and x >= c:
        return 1.0
    if x <= a or x >= c:
        return 0.0
    if x < b:
        return (x - a) / (b - a)
    if x > b:
        return (c - x) / (c - b)
    return 1.0


BUDGET_LOW = lambda x: triangular(x, 0, 0, 300000)
BUDGET_MEDIUM = lambda x: triangular(x, 50000, 300000, 700000)
BUDGET_HIGH = lambda x: triangular(x, 500000, 1000000, 1000000)


PC_LEVEL_LOW = lambda x: 1.0 if x == 1 else 0.0
PC_LEVEL_MEDIUM = lambda x: 1.0 if x == 2 else 0.0
PC_LEVEL_HIGH = lambda x: 1.0 if x == 3 else 0.0


PLAYTIME_SHORT = lambda x: triangular(x, 0, 0, 20)
PLAYTIME_MEDIUM = lambda x: triangular(x, 10, 45, 80)
PLAYTIME_LONG = lambda x: triangular(x, 60, 130, 200)


GAMER_CASUAL = lambda x: 1.0 if x == 1 else 0.0
GAMER_BALANCED = lambda x: 1.0 if x == 2 else 0.0
GAMER_HARDCORE = lambda x: 1.0 if x == 3 else 0.0


REC_NOT = lambda x: triangular(x, 0, 0, 25)
REC_LESS = lambda x: triangular(x, 20, 35, 50)
REC_YES = lambda x: triangular(x, 45, 60, 75)
REC_HIGH = lambda x: triangular(x, 70, 100, 100)
