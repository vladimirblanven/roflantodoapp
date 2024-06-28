from flask import Flask
from app.views import main_bp
from app.extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    app.register_blueprint(main_bp)
    return app