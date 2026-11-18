from src.todo import add_task, view_tasks

def test_add_task():
    add_task("Assignment", "High", "Study")

    tasks = view_tasks()

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Assignment"
    assert tasks[0]["priority"] == "High"
