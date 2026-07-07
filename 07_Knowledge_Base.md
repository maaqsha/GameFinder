# 07_Knowledge_Base.md

# Knowledge Base

## Purpose

This document defines the decision knowledge used to build the Fuzzy
Mamdani rule base. Every fuzzy rule must follow these principles.

------------------------------------------------------------------------

# KB-01 PC Compatibility

PC compatibility is the highest priority.

If the user's PC level is lower than the game's required PC level, the
recommendation must decrease significantly.

------------------------------------------------------------------------

# KB-02 Budget

Games within the user's budget are preferred.

Games exceeding the user's budget receive a lower recommendation.

------------------------------------------------------------------------

# KB-03 Rating

Games with higher Steam ratings are more desirable.

Low-rated games should rarely receive a high recommendation.

------------------------------------------------------------------------

# KB-04 Playtime

Games whose playtime matches the user's preference receive a higher
recommendation.

------------------------------------------------------------------------

# KB-05 Genre

Genre is not a fuzzy variable.

Genre is only used to filter candidate games before fuzzy inference.

------------------------------------------------------------------------

# KB-06 Priority Order

The importance of each variable is:

1.  PC Level
2.  Rating
3.  Budget
4.  Playtime

------------------------------------------------------------------------

# KB-07 Highly Recommended

A game should be classified as **Highly Recommended** only when almost
all important criteria match the user's preferences.

------------------------------------------------------------------------

# KB-08 Recommended

A game should be classified as **Recommended** when most criteria match
and no critical mismatch exists.

------------------------------------------------------------------------

# KB-09 Less Recommended

Used when several criteria partially match but one or more important
factors reduce suitability.

------------------------------------------------------------------------

# KB-10 Not Recommended

Assigned when there is a major mismatch, especially in PC compatibility
or multiple important criteria.

------------------------------------------------------------------------

# KB-11 Score Interpretation

Recommendation Score:

      Score Category
  --------- --------------------
      0--25 Not Recommended
     26--50 Less Recommended
     51--75 Recommended
    76--100 Highly Recommended

------------------------------------------------------------------------

# KB-12 Rule Consistency

-   Similar inputs should produce similar outputs.
-   No contradictory rules.
-   Every input combination must map to exactly one output.

------------------------------------------------------------------------

# KB-13 Scalability

Adding new games to the database must not require changes to the fuzzy
rule base.

------------------------------------------------------------------------

# KB-14 Explainability

Every recommendation should be explainable using these knowledge rules
rather than arbitrary scoring.

------------------------------------------------------------------------

# Conclusion

The complete 81-rule base must be generated according to this knowledge
base to ensure consistency, explainability, and maintainability.
