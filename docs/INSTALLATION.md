# Installation Guide

## Prerequisites

- Python 3.12+
- MySQL 8+
- Git

## Setup Steps

### 1. Clone Repository

```bash
git clone https://github.com/your-username/GameFinder.git
cd GameFinder
```

### 2. Database Setup

```bash
mysql -u root < dataset/import.sql
```

This creates database `gamefinder` and table `games`, then imports 600+ curated Steam game titles.

### 3. Python Environment

```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Configure Database Connection

Create or edit `.env` file in project root:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=gamefinder
```

### 5. Run Application

```bash
python run.py
```

Open http://127.0.0.1:5000 in browser.

## Running Tests

### Unit Tests (no database required)

```bash
python tests/test_recommendation.py
```

### Integration Tests (requires MySQL)

```bash
python tests/test_integration.py
```
