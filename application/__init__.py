"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .profile import profile
        from .home import home
        from .products import products
        from .assets import compile_static_assets

        app.register_blueprint(profile.account_bp)
        app.register_blueprint(home.home_bp)
        app.register_blueprint(products.product_bp)

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app
