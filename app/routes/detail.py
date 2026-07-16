# pyrefly: ignore [missing-import]
from flask import Blueprint, render_template, abort, request
import mysql.connector
from app.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from app.services.fuzzy.recommendation import _build_reasons as build_reasons

detail_bp = Blueprint('detail', __name__)


@detail_bp.route('/game/<int:app_id>')
def show(app_id):
    conn = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        'SELECT app_id, name, price_idr, rating_percentage, total_reviews, genre, tags, estimated_owners, peak_players FROM games WHERE app_id = %s',
        (app_id,),
    )
    game = cursor.fetchone()
    cursor.close()
    conn.close()

    if not game:
        abort(404)

    score = request.args.get('score')
    category = request.args.get('category')
    if score is not None:
        try:
            game['recommendation_score'] = float(score)
        except ValueError:
            pass
    if category:
        game['recommendation_category'] = category

    budget = request.args.get('budget', type=int)
    pc_level = request.args.get('pc_level', type=int)
    preferred_rating = request.args.get('preferred_rating', type=float)
    preferred_playtime = request.args.get('preferred_playtime', type=float)
    preferred_gamer_type = request.args.get('preferred_gamer_type', type=int)
    selected_genre = request.args.get('genre', '')

    reasons = None
    if budget is not None and pc_level is not None:
        reasons = build_reasons(
            game,
            budget,
            pc_level,
            preferred_rating or 75,
            preferred_playtime or 20,
            preferred_gamer_type or 2,
            selected_genre=selected_genre,
        )
    game['reasons'] = reasons

    game['release_year'] = None

    return render_template('detail.html', game=game)
