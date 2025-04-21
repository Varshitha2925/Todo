from bson import ObjectId
from app import mongo

tasks_collection = mongo.db.tasks

def get_all_tasks():
    return tasks_collection.find()

def insert_task(data):
    task = {
        "text": data["text"],
        "completed": False,
        "dueDate": data.get("dueDate"),
        "priority": data.get("priority", "Low")
    }
    inserted = tasks_collection.insert_one(task)
    return tasks_collection.find_one({"_id": inserted.inserted_id})

def toggle_task_complete(id):
    task = tasks_collection.find_one({"_id": ObjectId(id)})
    tasks_collection.update_one({"_id": ObjectId(id)}, {"$set": {"completed": not task["completed"]}})
    return tasks_collection.find_one({"_id": ObjectId(id)})

def update_task_details(id, data):
    tasks_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {
            "text": data["text"],
            "dueDate": data["dueDate"],
            "priority": data["priority"]
        }}
    )
    return tasks_collection.find_one({"_id": ObjectId(id)})

def delete_task_by_id(id):
    tasks_collection.delete_one({"_id": ObjectId(id)})
