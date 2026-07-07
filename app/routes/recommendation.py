from flask import Blueprint, render_template, request
from app.services.fuzzy.recommendation import recommend as rec_engine

recommendation_bp = Blueprint('recommendation', __name__)

@recommendation_bp.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'GET':
        return render_template('recommend.html')

    try:
        budget = int(request.form.get('budget', 300000))
        pc_level = int(request.form.get('pc_level', 2))
        preferred_rating = float(request.form.get('preferred_rating', 80))
        preferred_playtime = float(request.form.get('preferred_playtime', 20))
        genre = request.form.get('genre', 'Action')

        results = rec_engine(
            budget=budget,
            pc_level=pc_level,
            preferred_rating=preferred_rating,
            preferred_playtime=preferred_playtime,
            genre=genre,
            top_n=10,
        )

        form_data = {
            'budget': budget,
            'pc_level': pc_level,
            'preferred_rating': preferred_rating,
            'preferred_playtime': preferred_playtime,
            'genre': genre,
        }

        return render_template('results.html', results=results, form_data=form_data)

    except Exception as e:
        return render_template('error.html', message=str(e)), 500
