import os
import pytz
from flask import Blueprint, request, jsonify, render_template, send_from_directory
from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional

main_bp = Blueprint('main', __name__)

class Todo(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=1, max_length=75)
    description: Optional[str] = Field(None, max_length=150)
    created_at: str = Field(default_factory=lambda: datetime.now(pytz.utc).isoformat())

todos = {}
next_id = 1

def find_todo_by_id(todo_id: int):
    return todos.get(todo_id)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(main_bp.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@main_bp.route("/todos", methods=["GET"])
def get_todos():
    todos_list = [todo.dict() for todo in todos.values()]
    return jsonify(todos_list)

@main_bp.route("/todos", methods=["POST"])
def create_todo():
    global next_id
    try:
        todo_data = request.get_json()
        todo = Todo(
            id=next_id,
            title=todo_data.get('title'),
            description=todo_data.get('description')
        )

        todos[next_id] = todo
        next_id += 1

        return jsonify(todo.dict()), 201

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@main_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int):
    todo = find_todo_by_id(todo_id)
    if todo:
        return jsonify(todo.dict())
    return jsonify({"error": "ToDo not found"}), 404

@main_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    try:
        todo = todos.pop(todo_id, None)
        if todo:
            return jsonify(todo.dict())
        return jsonify({"error": "ToDo not found"}), 404

    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500
