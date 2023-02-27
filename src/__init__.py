import os
from flask import Flask
from flask_migrate import Migrate



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True, template_folder='templateFiles', static_folder='staticFiles')
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI='postgresql://root:root@localhost:5432/ntmanagement',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

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
    
    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import users, pages, patients
    app.register_blueprint(users.bp)
    app.register_blueprint(pages.bp)
    app.register_blueprint(patients.bp)

    return app