from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
import os
import logging
from logging.handlers import RotatingFileHandler


# Import your custom filter function here
def format_currency(value):
    return f'N{value:,.2f}'  # Format as Naira with two decimal places and comma separators


db = SQLAlchemy()
DB_NAME = "rently_web.db"

csrf = CSRFProtect()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rently_admin:rently@localhost/rently_web'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_pre_ping': True}
    app.config['UPLOAD_FOLDER'] = 'image_uploads'
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)  # Initialize SQLAlchemy

    # Initialize CSRF protection
    csrf.init_app(app)

    # Configure logging
    if not app.debug:
        log_handler = RotatingFileHandler('error.log', maxBytes=10240, backupCount=10)
        log_handler.setLevel(logging.ERROR)
        app.logger.addHandler(log_handler)

    # Register the custom filter
    app.jinja_env.filters['format_currency'] = format_currency

    # Import and register blueprints
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    # Create database tables within the application context
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import User
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists(os.path.join(app.root_path, DB_NAME)):
        with app.app_context():
            db.create_all()
            print('Created Database!')
