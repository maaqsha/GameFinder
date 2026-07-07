# 04_Fuzzy_Design.md

# Fuzzy Mamdani Design

## Overview

This document defines the fuzzy inference system used by the Steam Game
Recommendation System.

Method: **Fuzzy Mamdani**

Defuzzification: **Centroid**

------------------------------------------------------------------------

# Input Variables

## 1. Budget

Memberships:

-   Low
-   Medium
-   High

------------------------------------------------------------------------

## 2. PC Level

Memberships:

-   Low
-   Medium
-   High

------------------------------------------------------------------------

## 3. Preferred Rating

Memberships:

-   Low
-   Medium
-   High

------------------------------------------------------------------------

## 4. Preferred Playtime

Memberships:

-   Short
-   Medium
-   Long

------------------------------------------------------------------------

# Output Variable

## Recommendation Score

Memberships:

-   Not Recommended
-   Less Recommended
-   Recommended
-   Highly Recommended

Output Range:

0 - 100

------------------------------------------------------------------------

# Inference Process

``` text
User Input
      ↓
Fuzzification
      ↓
Rule Evaluation
      ↓
Aggregation
      ↓
Centroid Defuzzification
      ↓
Recommendation Score
```

------------------------------------------------------------------------

# Recommendation Categories

       Score Category
  ---------- --------------------
      0 - 25 Not Recommended
     26 - 50 Less Recommended
     51 - 75 Recommended
    76 - 100 Highly Recommended

------------------------------------------------------------------------

# Rule Base

The fuzzy engine uses:

-   4 input variables
-   3 membership functions for each input
-   Total possible combinations:

    3^4 = 81 Rules

All combinations are covered in the rule base.

------------------------------------------------------------------------

# Design Decisions

-   Genre is **not** a fuzzy variable.
-   Genre is used only to filter candidate games before fuzzy inference.
-   Every filtered game is evaluated independently.
-   Recommendation scores are sorted in descending order.
-   The Top 10 games are returned to the user.

------------------------------------------------------------------------

# Defuzzification

Method:

**Centroid (Center of Area)**

The centroid method converts the aggregated fuzzy output into a crisp
recommendation score.

------------------------------------------------------------------------

# Acceptance Criteria

-   All input variables participate in inference.
-   Every input combination matches at least one rule.
-   Every evaluated game receives a recommendation score.
-   Scores are generated in the range 0--100.
