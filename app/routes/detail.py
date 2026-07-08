from flask import Blueprint, render_template, abort, request
import mysql.connector
from app.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from app.services.fuzzy.recommendation import score_category, _build_reasons as build_reasons

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

    reasons = None
    if budget is not None and pc_level is not None:
        game['pc_level'] = pc_level
        game['playtime_hours'] = 15.0
        reasons = build_reasons(
            game,
            budget,
            pc_level,
            preferred_rating or 75,
            preferred_playtime or 20,
            preferred_gamer_type or 2,
        )
    game['reasons'] = reasons

    return render_template('detail.html', game=game)
