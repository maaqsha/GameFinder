# 06_Rule_Strategy.md

# Rule Strategy

## Purpose

This document defines how the 243 fuzzy rules are designed to ensure
consistency across the entire rule base.

------------------------------------------------------------------------

# Rule Formula

Each rule follows this format:

    IF
    Budget IS ...
    AND PC_Level IS ...
    AND Storage IS ...
    AND Rating IS ...
    AND Playtime IS ...

    THEN Recommendation IS ...

------------------------------------------------------------------------

# Input Variables

  Variable   Memberships
  ---------- ----------------------
  Budget     Low, Medium, High
  PC Level   Low, Medium, High
  Storage    Small, Medium, Large
  Rating     Low, Medium, High
  Playtime   Short, Medium, Long

Total combinations:

    3 × 3 × 3 × 3 × 3 = 243 Rules

------------------------------------------------------------------------

# Decision Priority

The recommendation priority is:

1.  PC Level
2.  Rating
3.  Budget
4.  Storage
5.  Playtime

PC compatibility has the highest impact because a game should not be
recommended if the user's PC cannot reasonably run it.

------------------------------------------------------------------------

# Output Levels

  Output               Meaning
  -------------------- ---------------------
  Not Recommended      Poor match
  Less Recommended     Below average match
  Recommended          Good match
  Highly Recommended   Excellent match

------------------------------------------------------------------------

# Rule Principles

## Highly Recommended

Typical conditions:

-   High PC compatibility
-   Rating is High
-   Budget is suitable
-   Storage is sufficient
-   Playtime matches user preference

------------------------------------------------------------------------

## Recommended

Typical conditions:

-   Most conditions match
-   One variable may be Medium

------------------------------------------------------------------------

## Less Recommended

Typical conditions:

-   Several Medium or Low matches
-   Recommendation is still possible

------------------------------------------------------------------------

## Not Recommended

Typical conditions:

-   PC compatibility is poor
-   Rating is low
-   Multiple important conditions do not match

------------------------------------------------------------------------

# Consistency Rules

-   Similar inputs should produce similar outputs.
-   No contradictory rules.
-   Every input combination must map to exactly one output.
-   All 243 combinations must be covered.

------------------------------------------------------------------------

# Validation Checklist

Before accepting the final rule base:

-   243 rules exist.
-   No duplicate rules.
-   No missing combinations.
-   No conflicting outputs.
-   Rule format is consistent.

------------------------------------------------------------------------

# Next Document

The next document (07_Rule_Base.md) will contain the complete set of 243
fuzzy rules following this strategy.
