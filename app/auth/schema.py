from marshmallow import fields, validate

from app.db import ma


class UserSchema(ma.Schema):
    username = fields.String()
    password = fields.String(validate=validate.Length(min=6))


class UserPOSTSchema(ma.Schema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)