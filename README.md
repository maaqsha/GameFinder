# Steam Game Recommendation System

A web-based Steam game recommendation system using **Fuzzy Mamdani** inference. Built with Flask, MySQL, and a 243-rule fuzzy engine.

## Architecture

```
User Input ──▶ Fuzzification ──▶ Inference (243 rules) ──▶ Aggregation ──▶ Defuzzification ──▶ Ranked Results
```

Five input dimensions: budget, PC level, gamer type, preferred rating, preferred playtime. Each game is scored against the user's profile, then sorted by score descending.

## Requirements

- Python 3.12+
- MySQL 8+
- Dependencies listed in `requirements.txt`

## Setup

### 1. Database

```bash
mysql -u root < dataset/import.sql
```

This creates the `gamefinder` database and `games` table, then imports 600+ curated Steam titles.

### 2. Python environment

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 3. Run

```bash
python run.py
```

Open http://127.0.0.1:5000

## Project Structure

```
app/
├── routes/                   # Flask blueprints (home, recommend, detail)
├── services/fuzzy/           # Fuzzy Mamdani engine
│   ├── membership.py         # Membership functions
│   ├── fuzzification.py      # Input → fuzzy sets
│   ├── inference.py          # 243-rule evaluation
│   ├── aggregation.py        # Rule output aggregation
│   ├── defuzzification.py    # Centroid defuzzification
│   └── recommendation.py     # Orchestration & scoring
├── templates/                # Jinja2 templates
├── static/                   # CSS, JS
tests/                        # Unit & integration tests
docs/                         # Design documentation
```

## Tests

```bash
# Unit tests (no database required)
python tests/test_recommendation.py

# Integration tests (MySQL required)
python tests/test_integration.py
```

## Documentation

Detailed design docs are in `docs/`:

- `01_Project_Overview.md` — Project summary and objectives
- `02_Functional_Requirements.md` — Functional requirements
- `03_Database_Design.md` — Schema and data sources
- `04_Fuzzy_Design.md` — Fuzzy Mamdani architecture
- `05_Membership_Function.md` — Membership function definitions
- `06_Rule_Strategy.md` — Rule base strategy
- `08_Project_Structure.md` — File structure reference
