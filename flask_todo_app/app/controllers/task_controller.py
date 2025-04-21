from flask import jsonify
from app.services.task_service import (
    get_all_tasks,
    insert_task,
    toggle_task_complete,
    update_task_details,
    delete_task_by_id
)
from app.models.task_model import task_to_json

def get_tasks():
    tasks = get_all_tasks()
    return jsonify([task_to_json(task) for task in tasks])

def create_task(data):
    new_task = insert_task(data)
    return jsonify(task_to_json(new_task))

def toggle_task(id):
    updated = toggle_task_complete(id)
    return jsonify(task_to_json(updated))

def update_task(id, data):
    updated = update_task_details(id, data)
    return jsonify(task_to_json(updated))

def delete_task(id):
    delete_task_by_id(id)
    return jsonify({"message": "Task deleted"})
