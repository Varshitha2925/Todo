from flask import Blueprint, request
from app.controllers.task_controller import (
    get_tasks, create_task, toggle_task, update_task, delete_task
)

task_routes = Blueprint("task_routes", __name__)

@task_routes.route("/")
def home():
    return {"message": "Flask API Connected"}

@task_routes.route("/tasks", methods=["GET"])
def fetch_tasks():
    return get_tasks()

@task_routes.route("/tasks", methods=["POST"])
def add_task():
    return create_task(request.json)

@task_routes.route("/tasks/<id>", methods=["PUT"])
def toggle_task_completion(id):
    return toggle_task(id)

@task_routes.route("/tasks/update/<id>", methods=["PUT"])
def edit_task(id):
    return update_task(id, request.json)

@task_routes.route("/tasks/<id>", methods=["DELETE"])
def remove_task(id):
    return delete_task(id)
