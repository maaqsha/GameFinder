# 08_Project_Structure.md

# Project Structure

## Overview

The project follows a modular Flask architecture. The Fuzzy Mamdani
engine is isolated from the web layer to improve maintainability and
testing.

------------------------------------------------------------------------

# Folder Structure

``` text
steam-game-recommendation/
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
│   ├── steamgames_clean.csv
│   ├── steamgames_clean_v3.csv
│   ├── steam_games_2024-2026.csv
│   └── import.sql
│
├── preprocessing/
│   ├── clean_data.py
│   ├── import_to_mysql.py
│   ├── reimport_db.py
│   └── ...
│
├── docs/
│
├── run.py
│
├── requirements.txt
│
└── README.md
```

------------------------------------------------------------------------

# Module Responsibilities

## Routes

Handle HTTP requests and responses.

## Models

Represent database entities.

## Services/Fuzzy

Contains the complete Fuzzy Mamdani implementation.

## Templates

Render user interface pages.

## Static

Stores CSS, JavaScript, and images.

## Dataset

Stores the original CSV dataset.

------------------------------------------------------------------------

# Core Principle

Business logic must remain inside the `services/fuzzy` module.

Routes must only: - Receive user input - Call the recommendation
service - Return results

------------------------------------------------------------------------

# Future Expansion

The architecture allows adding: - Steam API integration - User
accounts - Additional recommendation methods

without changing the fuzzy engine.
