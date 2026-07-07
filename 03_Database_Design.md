# 03_Database_Design.md

# Database Design

## Overview

The system uses a simple database design focused on supporting the Fuzzy
Mamdani recommendation process.

Only one table is required.

------------------------------------------------------------------------

# Database Schema

## Table: games

  Column              Type                          Description
  ------------------- ----------------------------- ------------------------------------
  app_id              BIGINT                        Steam App ID (Primary Key)
  name                VARCHAR(255)                  Game name
  price               DECIMAL(10,2)                 Game price
  positive            INT                           Positive reviews
  negative            INT                           Negative reviews
  rating_percentage   DECIMAL(5,2)                  Calculated rating percentage
  playtime            INT                           Average playtime forever (minutes)
  genre               VARCHAR(255)                  Game genres
  pc_level            ENUM('Low','Medium','High')   PC requirement level
  about               TEXT                          Game description
  header_image        TEXT                          Cover image URL
  website             TEXT                          Official website

------------------------------------------------------------------------

# Primary Key

-   app_id

------------------------------------------------------------------------

# Derived Columns

These values are generated during preprocessing.

## rating_percentage

Formula:

    positive / (positive + negative) * 100

## pc_level

Assigned manually or through preprocessing.

Values:

-   Low
-   Medium
-   High

------------------------------------------------------------------------

# Data Source

Dataset:

-   Steam Games Dataset

Imported as CSV during preprocessing.

------------------------------------------------------------------------

# Data Preprocessing

Before importing:

-   Remove duplicate App IDs.
-   Replace missing descriptions with an empty string.
-   Replace missing website URLs with NULL.
-   Calculate rating_percentage.
-   Assign pc_level.
-   Normalize genre values.

------------------------------------------------------------------------

# Query Flow

``` text
Load games
      ↓
Filter by genre
      ↓
Run Fuzzy Mamdani
      ↓
Calculate score
      ↓
Sort descending
      ↓
Return Top 10
```

------------------------------------------------------------------------

# Design Decision

This project intentionally uses a single-table database because the
focus is the Fuzzy Mamdani algorithm rather than relational database
complexity.
