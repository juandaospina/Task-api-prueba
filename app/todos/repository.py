from typing import List, Dict

from .models import Task
from app.auth.models import User
from app.exceptions import ObjectNotFound


def create_task(**task_data) -> Task:
    """
    Create a new task in the database.

    Parameters:
        title (str): Title of the task.
        description (str): Description of the task.

    Raises:
        ObjectNotFound: If the user is not found.
    
    Returns:
        Task: The created task object.
    """
    validate_user = User.get_by_id(task_data["user_id"])
    if not validate_user:
        raise ObjectNotFound("Usuario no encontrado.")
    
    task = Task(**task_data)
    task.create_object()
    return task


def get_tasks() -> List[Task]:
    """Return a list of tasks.

    Returns:
        List[Task]: List of all tasks.
    """
    tasks = Task.get_all()
    return tasks


def update_task(task_id: int, **task_data: Dict) -> Task:
    task = Task.get_by_id(id=task_id)
    if not task:
        raise ObjectNotFound()
    
    task.update(task_data)
    return task