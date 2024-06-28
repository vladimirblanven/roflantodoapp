from flask import Flask, jsonify
from app.views import main_bp
from app.extensions import db, ma
from pydantic import ValidationError

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    ma.init_app(app)
    app.register_blueprint(main_bp)

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        response = jsonify({"error": error.errors()})
        response.status_code = 400
        return response

    @app.errorhandler(Exception)
    def handle_exception(error):
        response = jsonify({"error": "An unexpected error occurred", "message": str(error)})
        response.status_code = 500
        return response

    return app
