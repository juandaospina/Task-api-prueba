from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


class BaseModelMixin:
    @classmethod
    def get_all(cls):
        return cls.query.all()
    
    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter(cls.task_id == id).first()
    

    def create_object(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            db.session.rollback()
            raise

    def update(self, data):
        if data:
            for key, value in data.items():
                setattr(self, key, value)
            db.session.commit()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise