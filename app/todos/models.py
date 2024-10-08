from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship 

from app.db import db, BaseModelMixin


class Task(db.Model, BaseModelMixin):
    __tablename__ = 'tasks' 

    task_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(65), nullable=False)
    description = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user_data = relationship("User")