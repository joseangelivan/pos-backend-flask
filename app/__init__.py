from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
cors = CORS()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'
    
    # Registrar blueprints
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Crear tablas de base de datos
    with app.app_context():
        db.create_all()
    
    return app

from app import models

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# db = SQLAlchemy()

# def create_app():
#     from .routes import auth, config

#     app = Flask(__name__)
#     app.config.from_object('config.Config')

#     CORS(app)
#     db.init_app(app)

#     app.register_blueprint(auth.bp)
#     app.register_blueprint(config.bp)

#     return app
