# 05_Membership_Function.md

# Membership Function Specification

## Overview

This document defines all membership functions used by the Fuzzy Mamdani
inference engine.

Membership Shape:

-   Triangular
-   Overlapping
-   Smooth transition between adjacent sets

------------------------------------------------------------------------

# 1. Budget (IDR)

Range: 0 -- 1,000,000

  Membership   Range
  ------------ ----------------------
  Low          0 -- 300,000
  Medium       200,000 -- 700,000
  High         600,000 -- 1,000,000

------------------------------------------------------------------------

# 2. PC Level

Range: 1 -- 3

    Value Meaning
  ------- ---------
        1 Low
        2 Medium
        3 High

PC Level uses crisp singleton membership — μ(x) = 1 when value matches, 0 otherwise. No triangular membership.

------------------------------------------------------------------------

# 3. Preferred Rating (%)

Range: 0 -- 100

  Membership   Range
  ------------ -----------
  Low          0 -- 75
  Medium       60 -- 90
  High         80 -- 100

------------------------------------------------------------------------

# 4. Preferred Playtime (Hours)

Range: 0 -- 200

  Membership   Range
  ------------ -----------
  Short        0 -- 20
  Medium       10 -- 80
  Long         60 -- 200

------------------------------------------------------------------------

# Output: Recommendation Score

Range: 0 -- 100

  Membership           Range
  -------------------- -----------
  Not Recommended      0 -- 25
  Less Recommended     20 -- 50
  Recommended          45 -- 75
  Highly Recommended   70 -- 100

------------------------------------------------------------------------

# Design Rules

-   Every adjacent membership overlaps.
-   All variables use the same inference method.
-   Centroid is used for defuzzification.
-   Membership values are normalized to 0--1 during computation.

------------------------------------------------------------------------

# Notes

These ranges are the official specification for the project. Any
implementation must follow this document unless the specification is
updated.
