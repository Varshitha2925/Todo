def task_to_json(task):
    return {
        "_id": str(task["_id"]),
        "text": task["text"],
        "completed": task["completed"],
        "dueDate": task.get("dueDate"),
        "priority": task.get("priority", "Low")
    }
