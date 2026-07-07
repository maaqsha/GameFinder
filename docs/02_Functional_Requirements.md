# 02_Functional_Requirements.md

# Functional Requirements

## Overview

This document defines all functional requirements for the Steam Game
Recommendation System.

The system has only one actor:

-   Guest User

No authentication or administrator module is included.

------------------------------------------------------------------------

# Functional Modules

## FR-01 Home Page

### Description

The system shall provide a landing page introducing the project.

### Requirements

-   Display project title.
-   Display project description.
-   Explain how the recommendation system works.
-   Provide a **Start Recommendation** button.

------------------------------------------------------------------------

## FR-02 Recommendation Form

### Input Fields

  ID   Field                            Required
  ---- -------------------------------- ----------
  F1   Budget                           Yes
  F2   Preferred Genre                  Yes
  F3   PC Level (Low / Medium / High)   Yes
  F4   Preferred Rating                 Yes
  F5   Preferred Playtime               Yes

### Requirements

-   Validate all inputs.
-   Prevent empty submission.
-   Display validation messages.

------------------------------------------------------------------------

## FR-03 Genre Filtering

Genre is used only as a database filter.

Requirements:

-   Filter games by selected genre.
-   Exclude games outside the selected genre.
-   Send filtered games to the fuzzy engine.

------------------------------------------------------------------------

## FR-04 Fuzzy Mamdani Engine

Process:

1.  Read user input.
2.  Perform fuzzification.
3.  Execute rule inference.
4.  Aggregate outputs.
5.  Perform centroid defuzzification.
6.  Generate recommendation score.

------------------------------------------------------------------------

## FR-05 Recommendation Ranking

Requirements:

-   Calculate scores for all filtered games.
-   Sort by score (highest first).
-   Display Top 10 recommendations.

------------------------------------------------------------------------

## FR-06 Recommendation Result

Display:

-   Rank
-   Game Name
-   Recommendation Score
-   Recommendation Category
-   View Detail button

------------------------------------------------------------------------

## FR-07 Game Detail

Display:

-   Cover Image
-   Game Name
-   Genre
-   Price
-   Steam Rating
-   Minimum PC Level
-   Estimated Playtime
-   Recommendation Score
-   Recommendation Explanation
-   Steam Store URL

------------------------------------------------------------------------

## FR-08 Recommendation Explanation

Example explanations:

-   Budget matches user preference.
-   PC level is sufficient.
-   Rating meets minimum requirement.
-   Playtime matches preference.

------------------------------------------------------------------------

# Business Rules

-   BR-01: Recommendation scores are generated using Fuzzy Mamdani.
-   BR-02: Genre filtering occurs before fuzzy calculation.
-   BR-03: Only filtered games are evaluated.
-   BR-04: Results are sorted in descending order.
-   BR-05: Display at most 10 recommendations.
-   BR-06: Empty input is not allowed.

------------------------------------------------------------------------

# Non-Functional Requirements

## Performance

-   Generate recommendations within 3 seconds for datasets up to 500
    games.

## Usability

-   Responsive interface.
-   Simple navigation.
-   Beginner-friendly layout.

## Reliability

-   Invalid input must not crash the application.

------------------------------------------------------------------------

# Acceptance Criteria

-   Users can submit all required inputs.
-   The fuzzy engine executes successfully.
-   Recommendation scores are generated.
-   Top 10 games are displayed.
-   Detail pages display complete information.
-   Recommendation explanations are shown correctly.
