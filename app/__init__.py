from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app.extensions import mail, csrf

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Ensure Flask is using config.py

    mail.init_app(app)
    csrf.init_app(app)

    db.init_app(app)


    from app.routes import main
    app.register_blueprint(main)

    return app
