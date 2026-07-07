from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    with app.app_context():
        from app.routes.home import home_bp
        from app.routes.recommendation import recommendation_bp
        from app.routes.detail import detail_bp

        app.register_blueprint(home_bp)
        app.register_blueprint(recommendation_bp)
        app.register_blueprint(detail_bp)

    return app
