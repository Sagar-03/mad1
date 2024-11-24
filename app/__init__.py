from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)

    # Import and register blueprints
    from app.routes import admin_routes, customer_routes, professional_routes
    app.register_blueprint(admin_routes.bp)
    app.register_blueprint(customer_routes.bp)
    app.register_blueprint(professional_routes.bp)

    return app
