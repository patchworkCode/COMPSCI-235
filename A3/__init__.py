import os

from flask import Flask


def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)

    with app.app_context():
        # Register blueprints.
        from .movie_blueprint import movie
        app.register_blueprint(movie.movie_blueprint)

    return app
