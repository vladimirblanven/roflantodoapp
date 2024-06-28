from functools import wraps
from flask import jsonify

def error_handler(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValidationError as e:
            response = jsonify({"error": e.errors()})
            response.status_code = 400
            return response
        except Exception as e:
            response = jsonify({"error": "An unexpected error occurred", "message": str(e)})
            response.status_code = 500
            return response
    return decorated_function
