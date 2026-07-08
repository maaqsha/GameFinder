# 10_Task_List.md

# AI Development Task List

## Purpose

This document defines the implementation order for the AI coding
assistant.

Complete each task sequentially. Do not skip tasks. Ask for confirmation
before moving to the next major phase.

------------------------------------------------------------------------

# Phase 1 --- Project Initialization

## Task 1

-   Create Flask project.
-   Create the folder structure.
-   Install dependencies.
-   Verify the application runs.

Deliverable: - Running Flask project.

------------------------------------------------------------------------

# Phase 2 --- Dataset Preparation

## Task 2

-   Load `steamgamesdataset.csv`.
-   Keep only required columns.
-   Remove duplicate App IDs.
-   Handle missing values.
-   Generate `rating_percentage`.
-   Generate `pc_level`.

Deliverable: - Clean dataset.

------------------------------------------------------------------------

# Phase 3 --- Database

## Task 3

-   Create MySQL database.
-   Create `games` table.
-   Import cleaned dataset.
-   Verify imported records.

Deliverable: - Working database.

------------------------------------------------------------------------

# Phase 4 --- Fuzzy Engine

## Task 4

Implement: - Membership Function - Fuzzification - Rule Inference -
Aggregation - Centroid Defuzzification

Deliverable: - Working Fuzzy Mamdani engine.

------------------------------------------------------------------------

# Phase 5 --- Rule Base

## Task 5

-   Generate all 243 rules (3⁵ budget × pc_level × gamer_type × rating × playtime).
-   Validate all combinations.
-   Ensure no duplicate or conflicting rules.

Deliverable: - Validated rule base.

------------------------------------------------------------------------

# Phase 6 --- Recommendation Engine

## Task 6

-   Filter by genre.
-   Evaluate all candidate games.
-   Rank results.
-   Return Top 10.

Deliverable: - Recommendation engine.

------------------------------------------------------------------------

# Phase 7 --- User Interface

## Task 7

Create: - Home - Recommendation Form - Result - Detail

Deliverable: - Responsive UI.

------------------------------------------------------------------------

# Phase 8 --- Integration

## Task 8

Integrate: - UI - Database - Fuzzy Engine

Deliverable: - End-to-end application.

------------------------------------------------------------------------

# Phase 9 --- Testing

## Task 9

Test: - Validation - Fuzzy calculation - Ranking - Detail page - Error
handling

Deliverable: - Stable application.

------------------------------------------------------------------------

# Phase 10 --- Final Review

## Task 10

-   Refactor code.
-   Remove unused code.
-   Final verification.
-   Update documentation.

Deliverable: - Completed project.

------------------------------------------------------------------------

# Rules

-   Follow every document inside `docs/`.
-   Do not redesign the architecture.
-   Complete one phase at a time.
-   Report completion after each phase.
