import pytest
from src.todo import add_task, view_tasks

def test_add_task():
    add_task("Assignment", "High", "Study")

    tasks = view_tasks()

    assert len(tasks) >= 1

def test_empty_title():

    with pytest.raises(ValueError):
        add_task("", "High", "Study")
