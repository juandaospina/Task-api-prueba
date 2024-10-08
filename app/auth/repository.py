from typing import Dict

from .models import User
from app.errors_handling import ObjectNotFound


def get_user(username: int) -> User:
    """Returns"""
    user = User.query.filter(User.username == username).first()
    if user is None:
        raise ObjectNotFound()
    return user


def create_user(**user_data: Dict):
    """Create a new user.
    """
    user = User(**user_data)
    user.create_object()
    return user