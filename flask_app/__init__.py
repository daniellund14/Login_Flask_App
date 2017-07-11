from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.sqlite'
    db.init_app(app)
    db.app = app
    db.create_all()
    return app


