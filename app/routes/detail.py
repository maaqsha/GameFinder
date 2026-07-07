from flask import Blueprint, render_template, abort, request
import mysql.connector
from app.config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

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
        'SELECT app_id, name, price_idr, rating_percentage, playtime_hours, genre, pc_level, header_image, short_description FROM games WHERE app_id = %s',
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

    return render_template('detail.html', game=game)
