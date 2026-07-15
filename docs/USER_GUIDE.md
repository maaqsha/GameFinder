# User Guide

## How to Get Game Recommendations

### 1. Open the Application

Navigate to http://127.0.0.1:5000 in your browser.

### 2. Click "Mulai Rekomendasi"

On the home page, click the button to start the recommendation process.

### 3. Fill the Recommendation Form

Provide the following inputs:

| Field          | Description                                      | Options                      |
|----------------|--------------------------------------------------|------------------------------|
| Budget         | Maximum amount you want to spend (IDR)           | Any positive number          |
| Genre          | Game genre preference                            | Action, RPG, Strategy, etc.  |
| PC Level       | Your computer's capability                       | Low / Medium / High          |
| Gamer Type     | Your gaming preference profile                   | Casual / Balanced / Hardcore |
| Preferred Rating | Minimum Steam rating you want                  | 0 – 100%                     |
| Playtime       | How long you want to play per session            | Short / Medium / Long        |

### 4. View Results

Results page shows Top 10 recommended games sorted by recommendation score:

- **Rank** — Position in the list
- **Game Name** — Click to view details
- **Price** — Game price in IDR
- **Rating** — Steam rating percentage
- **Score** — Fuzzy recommendation score (0–100)
- **Category** — Not Recommended / Less Recommended / Recommended / Highly Recommended

### 5. View Game Details

Click a game name to see:

- Cover image
- Full description
- Genre and tags
- Price
- Steam rating with review counts
- Required PC level
- Recommendation explanation (why this game matches your profile)
- Steam Store link

## Understanding Scores

| Score Range | Category           | Meaning                                  |
|-------------|--------------------|------------------------------------------|
| 0 – 25      | Not Recommended    | Poor match with your preferences         |
| 26 – 50     | Less Recommended   | Below-average match                      |
| 51 – 75     | Recommended        | Good match                               |
| 76 – 100    | Highly Recommended | Excellent match with most criteria       |

## Tips

- **No budget limit?** Enter a high number (e.g., 1000000) to see all games.
- **Want free games only?** Set budget to 0.
- **Not sure about genre?** Leave it empty to see games across all genres.
- **Casual gamer?** Select Casual — system prioritizes lower-budget games with decent ratings.
- **Hardcore gamer?** Select Hardcore — system prioritizes higher-budget, top-rated games.
