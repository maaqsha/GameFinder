# System Architecture

## Overview

Project follows modular Flask architecture. Fuzzy Mamdani engine isolated from web layer for maintainability and testability.

## Directory Structure

```
GameFinder/
│
├── app/
│   ├── routes/
│   │   ├── home.py
│   │   ├── recommendation.py
│   │   └── detail.py
│   │
│   ├── services/
│   │   └── fuzzy/
│   │       ├── membership.py
│   │       ├── fuzzification.py
│   │       ├── inference.py
│   │       ├── aggregation.py
│   │       ├── defuzzification.py
│   │       └── recommendation.py
│   │
│   ├── models/
│   │   └── game.py
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── recommend.html
│   │   ├── results.html
│   │   ├── detail.html
│   │   ├── error.html
│   │   └── components/
│   │       ├── navbar.html
│   │       ├── footer.html
│   │       └── game_card.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── theme.js
│   │
│   └── utils/
│
├── dataset/
│   └── import.sql
│
├── tests/
│
├── docs/
│
├── run.py
│
├── requirements.txt
│
└── README.md
```

## Module Responsibilities

### Routes
Handle HTTP requests and responses only.

- `home.py` — Landing page
- `recommendation.py` — Form submission, fuzzy evaluation orchestration, results
- `detail.py` — Game detail page with recommendation explanation

### Services / Fuzzy
Contains complete Fuzzy Mamdani implementation. Business logic stays here.

- `membership.py` — Membership function definitions
- `fuzzification.py` — Input value to fuzzy set conversion
- `inference.py` — 243-rule generation and evaluation
- `aggregation.py` — Output aggregation across rules
- `defuzzification.py` — Centroid defuzzification
- `recommendation.py` — Orchestrates end-to-end recommendation pipeline

### Models
Database entity representation.

### Templates
Jinja2 rendering for all UI pages.

### Static
CSS, JavaScript, and assets.

## Database Schema

Single-table design — intentional. Focus is on fuzzy algorithm, not relational complexity.

### Table: `games`

| Column            | Type            | Description                              |
|-------------------|-----------------|------------------------------------------|
| app_id            | BIGINT          | Steam App ID (Primary Key)               |
| name              | VARCHAR(255)    | Game name                                |
| price_idr         | DECIMAL(10,2)   | Price in IDR                             |
| positive          | INT             | Positive reviews                         |
| negative          | INT             | Negative reviews                         |
| rating_percentage | DECIMAL(5,2)    | Calculated rating percentage             |
| playtime_hours    | DECIMAL(8,2)    | Average playtime (hours)                 |
| genre             | VARCHAR(255)    | Game genre                               |
| tags              | TEXT            | Additional tags for filtering            |
| pc_level          | TINYINT         | PC requirement level (1=Low, 2=Medium, 3=High) |
| about             | TEXT            | Game description                         |
| header_image      | TEXT            | Cover image URL                          |
| website           | TEXT            | Official website                         |

### Derived Columns

**rating_percentage:**
```
positive / (positive + negative) * 100
```

**pc_level:**
- 1 = Low
- 2 = Medium
- 3 = High

### Data Source

Steam Games Dataset, imported as CSV after preprocessing.

### Preprocessing Steps

Before import:
- Remove duplicate App IDs
- Replace missing descriptions with empty string
- Replace missing website URLs with NULL
- Price stored directly in IDR (no USD conversion)
- Convert average playtime from minutes to hours
- Calculate rating_percentage
- Assign pc_level as INTEGER (1, 2, or 3)
- Normalize genre values

### Query Flow

``` text
Load games
      ↓
Filter by genre + budget
      ↓
Fuzzy Mamdani evaluation
      ↓
Calculate score
      ↓
Sort descending
      ↓
Return Top 10
```

## Design Principles

- Business logic in `services/fuzzy` only
- Routes only: receive input → validate → call service → return response
- Adding new games does not require fuzzy rule changes
- Single database table keeps focus on fuzzy algorithm
