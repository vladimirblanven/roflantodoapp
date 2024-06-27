from flask import Blueprint, request, jsonify, render_template
from app.models import Todo
from app.extensions import db
from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional

main_bp = Blueprint('main', __name__)

class TodoSchema(BaseModel):
    id: Optional[int]
    title: str = Field(..., min_length=1, max_length=75)
    description: Optional[str] = Field(None, max_length=150)
    created_at: Optional[str]

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/todos", methods=["GET"])
def get_todos():
    todos = Todo.query.all()
    todos_list = [todo.to_dict() for todo in todos]
    return jsonify(todos_list)

@main_bp.route("/todos", methods=["POST"])
def create_todo():
    try:
        todo_data = request.get_json()
        todo = Todo(
            title=todo_data.get('title'),
            description=todo_data.get('description')
        )
        db.session.add(todo)
        db.session.commit()
        return jsonify(todo.to_dict()), 201
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500

@main_bp.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify(todo.to_dict())
    return jsonify({"error": "ToDo not found"}), 404

@main_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    try:
        todo = Todo.query.get(todo_id)
        if (todo):
            db.session.delete(todo)
            db.session.commit()
            return jsonify(todo.to_dict())
        return jsonify({"error": "ToDo not found"}), 404
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred"}), 500