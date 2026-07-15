# Fuzzy Mamdani Logic

## Overview

Defines the fuzzy inference system used by the Steam Game Recommendation System.

- **Method**: Fuzzy Mamdani
- **Defuzzification**: Centroid (Center of Area)

## Input Variables

### 1. Budget (IDR)

Membership functions — triangular:

| Category | Shape (a, b, c) |
|----------|-----------------|
| Low      | 0, 0, 300,000   |
| Medium   | 50,000, 300,000, 700,000 |
| High     | 500,000, 1,000,000, 1,000,000 |

Overlap: Low-Medium at Rp50,000–Rp300,000. Medium-High at Rp500,000–Rp700,000.

### 2. PC Level

Crisp singleton — not fuzzy. μ(x) = 1 if value matches, 0 otherwise.

| Value | Meaning |
|-------|---------|
| 1     | Low     |
| 2     | Medium  |
| 3     | High    |

### 3. Gamer Type

Defines the ideal combination of budget / rating / playtime preferences.

| Type     | Budget | Rating | Playtime |
|----------|--------|--------|----------|
| Casual   | Low    | Medium | Medium   |
| Balanced | Medium | High   | Medium   |
| Hardcore | High   | High   | Medium   |

### 4. Preferred Rating (%)

Dynamic triangular functions relative to user's `preferred_rating` (p):

| Category | Shape (a, b, c)      |
|----------|----------------------|
| Low      | 0, 0, p+20           |
| Medium   | p-25, p-5, p+25      |
| High     | p-15, 100, 100       |

High has right shoulder at 100 (does not descend to 0).

### 5. Preferred Playtime (hours)

Playtime is neutralized — all gamer types use Medium. No real playtime data from dataset.

| Category | Shape (a, b, c) |
|----------|-----------------|
| Short    | 0, 0, 20        |
| Medium   | 10, 40, 80      |
| Long     | 60, 200, 200    |

## Output Variable

### Recommendation Score

Range: 0 – 100

| Category              | Score Range |
|-----------------------|-------------|
| Not Recommended       | 0 – 25      |
| Less Recommended      | 20 – 50     |
| Recommended           | 45 – 75     |
| Highly Recommended    | 70 – 100    |

## Inference Process

``` text
User Input
      ↓
Fuzzification
      ↓
Rule Evaluation (243 rules)
      ↓
Aggregation
      ↓
Centroid Defuzzification
      ↓
Recommendation Score
```

## Rule Base

- 5 input variables
- 3 membership functions per input
- Total: 3^5 = **243 rules**
- Every combination covered exactly once

### Rule Format

```
IF Budget IS Low AND PC_Level IS Low AND Gamer_Type IS Casual AND Rating IS Low AND Playtime IS Medium
THEN Recommendation IS Less Recommended
```

### Output Calculation

Each game is evaluated independently. Score derived from centroid of aggregated rule outputs across 4 categories.

### Match Counting (Score Mapping)

| Matches | Category Index |
|---------|----------------|
| 3/3     | 3 — Highly Recommended |
| 2/3     | 2 — Recommended |
| 1/3     | 1 — Less Recommended |
| 0/3     | 0 — Not Recommended |

3 dimensions counted: budget match, rating match, playtime match. PC level is in antecedents (firing via `min()`) but excluded from match counting — it represents hardware capability, not preference.

## Decision Priority

1. **Gamer Type** — determines ideal budget/rating/playtime profile
2. **Rating** — higher-rated games preferred
3. **Budget** — games within budget prioritized
4. **Playtime** — neutralized (all profiles use Medium)

## Knowledge Base

### KB-01 Gamer Type Alignment
Gamer type is highest priority — defines ideal budget/rating/playtime combination.

### KB-02 Budget
Games within user budget range are prioritized. Games exceeding budget receive lower scores.

### KB-03 Rating
Higher Steam rating is preferred. Low-rated games rarely receive high recommendations.

### KB-04 Playtime
Playtime matching user preference scores higher. Currently neutralized (no real playtime data).

### KB-05 Genre
Genre is NOT a fuzzy variable. Used only as SQL pre-filter before fuzzy inference.

### KB-06 Priority Order
1. Gamer Type → 2. Rating → 3. Budget → 4. Playtime

### KB-07 Highly Recommended
Only when nearly all criteria match user preferences.

### KB-08 Recommended
When most criteria match with no critical mismatches.

### KB-09 Less Recommended
When some criteria partially match or one+ important factors reduce fit.

### KB-10 Not Recommended
Major mismatch in gamer type, low rating, or multiple criteria unmet.

### KB-11 Score Interpretation
See output variable table above.

### KB-12 Rule Consistency
Similar inputs produce similar outputs. No conflicting rules. Every input combination maps to exactly one output.

### KB-13 Scalability
Adding new games requires no changes to fuzzy rule base.

### KB-14 Explainability
Every recommendation must be explainable using knowledge rules.

## Design Decisions

- Genre is a database filter only — not fuzzy input
- PC level in antecedents but excluded from match counting (hardware, not preference)
- Playtime neutralized via `playtime_hours=preferred_playtime` — keeps 243-rule architecture intact without fabricated data
- Gamer type profiles represent player preference, not hardware capability
- Overlapping input MFs create multi-category firings, producing continuous score spread via centroid

## Acceptance Criteria

- All input variables participate in inference
- Every input combination matches at least one rule
- Each evaluated game receives a recommendation score
- Scores in 0–100 range
- Top 10 returned sorted descending by score
