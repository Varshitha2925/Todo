from flask import Blueprint, request, jsonify
from bson import ObjectId
from . import mongo
from .models import task_to_json

main = Blueprint("main", __name__)
tasks_collection = mongo.db.tasks

@main.route("/")
def home():
    return jsonify({"message": "Flask API Connected"})

@main.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = tasks_collection.find()
    return jsonify([task_to_json(task) for task in tasks])

@main.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = {
        "text": data["text"],
        "completed": False,
        "dueDate": data.get("dueDate"),
        "priority": data.get("priority", "Low")
    }
    inserted = tasks_collection.insert_one(task)
    new_task = tasks_collection.find_one({"_id": inserted.inserted_id})
    return jsonify(task_to_json(new_task))

@main.route("/tasks/<id>", methods=["PUT"])
def toggle_complete(id):
    task = tasks_collection.find_one({"_id": ObjectId(id)})
    tasks_collection.update_one({"_id": ObjectId(id)}, {"$set": {"completed": not task["completed"]}})
    updated_task = tasks_collection.find_one({"_id": ObjectId(id)})
    return jsonify(task_to_json(updated_task))

@main.route("/tasks/update/<id>", methods=["PUT"])
def update_task(id):
    data = request.json
    tasks_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "text": data["text"],
            "dueDate": data["dueDate"],
            "priority": data["priority"]
        }}
    )
    updated_task = tasks_collection.find_one({"_id": ObjectId(id)})
    return jsonify(task_to_json(updated_task))

@main.route("/tasks/<id>", methods=["DELETE"])
def delete_task(id):
    tasks_collection.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Task deleted"})