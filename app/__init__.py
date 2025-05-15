from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    from .routes import auth, config

    app = Flask(__name__)
    app.config.from_object('config.Config')

    CORS(app)
    db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(config.bp)

    return app
