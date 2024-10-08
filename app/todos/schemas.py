from marshmallow import fields, validate

from app.db import ma


class TaskPOSTSchema(ma.Schema):
    title = fields.String(validate=validate.Length(min=1, max=100), 
                          allow_none=False)
    description = fields.String(required=False)
    user_id = fields.Integer(required=True)


class TaskSchema(TaskPOSTSchema):
    task_id = fields.Integer(dump_only=True)


class TaskPUTSchema(ma.Schema):
    title = fields.String(validate=validate.Length(min=1, max=100))
    description = fields.String()