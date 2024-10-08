from sqlalchemy import Column, Integer, String, DateTime, func

from app.db import BaseModelMixin, db


class User(db.Model, BaseModelMixin):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime(), server_default=func.now())

    def __str__(self) -> str:
        return f"Value: {self.first_name}"
    
    def __repr__(self) -> str:
        return f"User('{self.first_name}')"