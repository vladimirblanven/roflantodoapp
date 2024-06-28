from flask import Blueprint, request, jsonify, render_template
from app.models import Todo
from app.extensions import db
from app.utils import get_first_available_id
from app.error_handler import error_handler
from pydantic import BaseModel, ValidationError, Field
from datetime import datetime
from typing import Optional

main_bp = Blueprint('main', __name__)

class TodoSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=75)
    description: Optional[str] = Field(None, max_length=150)

@main_bp.route("/")
@error_handler
def index():
    return render_template("index.html")

@main_bp.route("/todos", methods=["GET"])
@error_handler
def get_todos():
    todos = Todo.query.all()
    todos_list = [todo.to_dict() for todo in todos]
    return jsonify(todos_list)

@main_bp.route("/todos", methods=["POST"])
@error_handler
def create_todo():
    todo_data = request.get_json()
    validated_data = TodoSchema(**todo_data)

    todo = Todo(
        id=get_first_available_id(),
        title=validated_data.title,
        description=validated_data.description
    )
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201

@main_bp.route("/todos/<int:todo_id>", methods=["GET"])
@error_handler
def get_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if todo:
        return jsonify(todo.to_dict())
    return jsonify({"error": "ToDo not found"}), 404

@main_bp.route("/todos/<int:todo_id>", methods=["DELETE"])
@error_handler
def delete_todo(todo_id: int):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return jsonify(todo.to_dict())
    return jsonify({"error": "ToDo not found"}), 404
