from marshmallow import Schema, fields


class ResponseSchema(Schema):
    message = fields.String(load_default="¡Registro creado con éxito!")