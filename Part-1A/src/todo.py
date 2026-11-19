import json

tasks = []

def add_task(title, priority, tag):
    if not title:
        raise ValueError("Task title cannot be empty")

    task = {
        "title": title,
        "priority": priority,
        "tag": tag
    }

    tasks.append(task)
    return task
    
def view_tasks():
    return tasks

def save_tasks(filename="tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)
