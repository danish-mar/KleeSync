import os
from flask import Flask
from app.extensions import db
from app.routes import register_blueprints
from app.config import config


def create_app():
    app = Flask(__name__)

    # gets the environment from the environment variable
    env = os.getenv("FLASK_ENV", "development")

    # loads the config
    app.config.from_object(config[env])

    # initializes the db object
    db.init_app(app)

    # initializes the app context here
    with app.app_context():

        register_blueprints(app)

    return app
