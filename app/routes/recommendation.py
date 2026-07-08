from flask import Blueprint, render_template, request
from app.services.fuzzy.recommendation import recommend as rec_engine
import mysql.connector

recommendation_bp = Blueprint('recommendation', __name__)


def _get_max_budget():
    try:
        conn = mysql.connector.connect(
            host='localhost', user='root', password='', database='gamefinder',
        )
        cursor = conn.cursor()
        cursor.execute('SELECT MAX(price_idr) FROM games')
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row and row[0]:
            max_val = int(row[0])
            # Round up to next 100K
            return ((max_val // 100000) + 1) * 100000
        return 10000000
    except Exception:
        return 10000000


@recommendation_bp.route('/recommend', methods=['GET', 'POST'])
def recommend():
    max_budget = _get_max_budget()

    if request.method == 'GET':
        return render_template('recommend.html', max_budget=max_budget)

    try:
        budget = int(request.form.get('budget', 300000))
        pc_level = int(request.form.get('pc_level', 2))
        preferred_rating = float(request.form.get('preferred_rating', 80))
        preferred_playtime = float(request.form.get('preferred_playtime', 30))
        preferred_gamer_type = int(request.form.get('gamer_type', 2))
        genre = request.form.get('genre', 'Action')
        if not genre.strip():
            genre = 'Action'

        results = rec_engine(
            budget=budget,
            pc_level=pc_level,
            preferred_rating=preferred_rating,
            preferred_playtime=preferred_playtime,
            genre=genre,
            top_n=10,
            preferred_gamer_type=preferred_gamer_type,
        )

        form_data = {
            'budget': budget,
            'pc_level': pc_level,
            'preferred_rating': preferred_rating,
            'preferred_playtime': preferred_playtime,
            'preferred_gamer_type': preferred_gamer_type,
            'genre': genre,
        }

        return render_template('results.html', results=results, form_data=form_data)

    except Exception as e:
        return render_template('error.html', message=str(e)), 500
