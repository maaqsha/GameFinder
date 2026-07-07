# 11_AI_RULES.md

# AI Coding Rules

## Purpose

This document defines how the AI coding assistant must behave while
developing the project.

These rules are mandatory.

------------------------------------------------------------------------

# Rule 1

Read every document inside the `docs/` folder before writing any code.

------------------------------------------------------------------------

# Rule 2

Do not change the project scope unless explicitly instructed.

------------------------------------------------------------------------

# Rule 3

Do not redesign the architecture.

Follow the documented folder structure.

------------------------------------------------------------------------

# Rule 4

Do not add features that are outside the documented scope.

Examples:

-   Login
-   Registration
-   Admin Dashboard
-   Steam API
-   Payment System
-   Machine Learning
-   Deep Learning

------------------------------------------------------------------------

# Rule 5

Always follow the implementation order defined in `10_Task_List.md`.

------------------------------------------------------------------------

# Rule 6

Complete one major task at a time.

Do not work on multiple major phases simultaneously.

------------------------------------------------------------------------

# Rule 7

Business logic belongs only inside the Fuzzy service module.

Routes should only:

-   Receive requests
-   Validate input
-   Call services
-   Return responses

------------------------------------------------------------------------

# Rule 8

Do not use third-party fuzzy logic libraries.

Implement the complete Fuzzy Mamdani algorithm manually.

------------------------------------------------------------------------

# Rule 9

If documentation conflicts are found:

-   Stop implementation.
-   Explain the conflict.
-   Ask for clarification.

Never guess.

------------------------------------------------------------------------

# Rule 10

If information is missing:

-   Make the smallest reasonable assumption.
-   Clearly document that assumption.
-   Continue only if it does not affect the architecture.

------------------------------------------------------------------------

# Rule 11

Generate clean Python code.

Requirements:

-   Follow PEP 8
-   Small functions
-   Reusable code
-   Meaningful names
-   Avoid duplication

------------------------------------------------------------------------

# Rule 12

Before completing each phase:

Verify:

-   No syntax errors
-   No runtime errors
-   No missing imports
-   No broken routes

------------------------------------------------------------------------

# Rule 13

After finishing a phase:

Provide:

-   Completed tasks
-   Files created
-   Important implementation notes
-   Remaining work

Wait for user confirmation before starting the next major phase.

------------------------------------------------------------------------

# Rule 14

When generating the fuzzy rule base:

-   Cover all 243 combinations.
-   No duplicate rules.
-   No conflicting outputs.
-   Follow:
    -   Membership Function
    -   Rule Strategy
    -   Knowledge Base

------------------------------------------------------------------------

# Rule 15

Project Goal

The objective is not to build the most complex website.

The objective is to correctly implement the Fuzzy Mamdani recommendation
algorithm in a clean, maintainable Flask application.

Always prioritize correctness, simplicity, and consistency over
unnecessary complexity.
