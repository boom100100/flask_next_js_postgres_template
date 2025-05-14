import os

from flask import Flask
from flask_migrate import Migrate

from app.constants import DB_URI, SECRET_KEY
from app.database import db
from app.models import Example
from app.views.routes import api_v1_blueprint, app_blueprint


migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

    for package in (
        db,
    ):
        package.init_app(app)
    migrate.init_app(app, db)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(app_blueprint, url_prefix='/')
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app


app = create_app()
if __name__ == "__main__":
    app.run()
