import os

from flask import Flask

import A3.adapters.repository as repo
from A3.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config=None):
    """Construct the core application."""

    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('A3', 'adapters', 'Data')

    if test_config is not None:
        # Load test configuration, and overrride any configuration settings.
        app.config.from_mapping(test_config)
        data_path = os.path.join('C:', os.sep, 'Users', 'idenf', 'Documents', 'GitHub', 'tests', 'data')

    # Create the MemoryRepository implementation for a memory-based repository.
    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)


    with app.app_context():
        # Register blueprints.
        from .blueprints import movies, home
        app.register_blueprint(movies.movie_blueprint)
        app.register_blueprint(home.home_blueprint)
        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

    return app
