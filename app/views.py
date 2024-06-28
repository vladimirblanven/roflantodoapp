from flask import Blueprint, request, jsonify, render_template
from app.models import Todo, TodoSchema
from app.extensions import db
from app.utils import get_first_available_id
from marshmallow import ValidationError

main_bp = Blueprint('main', __name__)

todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    return jsonify(todos_schema.dump(todos))

@main_bp.route("/todos", methods=["POST"])
def create_todo():
    try:
        todo_data = request.get_json()
        validated_data = todo_schema.load(todo_data)

        todo = Todo(
            id=get_first_available_id(),
            title=validated_data.title,
            description=validated_data.description
        )
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo_schema.dump(todo)), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@main_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify(todo_schema.dump(todo))
    return jsonify({"error": "ToDo not found"}), 404

@main_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify(todo_schema.dump(todo))
    return jsonify({"error": "ToDo not found"}), 404