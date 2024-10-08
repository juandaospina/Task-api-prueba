from flask import Blueprint
from flask_apispec import views, doc, use_kwargs, marshal_with
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token

from app.errors_handling import Unauthorized
from app.docs import docs
from app.common import ResponseSchema
from .schema import UserSchema, UserPOSTSchema
from . import repository


jwt_bp = Blueprint("jwt", __name__, url_prefix="/v1")
api = Api(jwt_bp)


@doc(tags=["Authorization"])
class UsersResource(views.MethodResource, Resource):
    @doc(description='Create a new user in the database.', responses={
        422: {"description": "Entidad no procesable"},
    })
    @marshal_with(ResponseSchema, code=200)
    @use_kwargs(UserPOSTSchema, location='json')
    def post(self, **kwargs):
        repository.create_user(**kwargs)
        return ResponseSchema().load(
            {'message': '¡Usuario creado existosamente!'}), 200


@doc(tags=["Authorization"], responses={
    401: {"description": "Usuario no autorizado"},
    404: {"description": "Objecto no encontrado"}})
class TokenResource(views.MethodResource, Resource):
    @doc(description="Get authorization token")
    @use_kwargs(UserSchema, location="json")
    def post(self, **kwargs):
        username = kwargs.get("username")
        user = repository.get_user(username)
        if user.password != kwargs.get("password"):
            raise Unauthorized()
        token = create_access_token(identity=user.username)
        return {"access_token": token}, 200
    

# Register resources
api.add_resource(TokenResource, "/login")
api.add_resource(UsersResource, "/users/register")
# Register documentation
docs.register(TokenResource, blueprint=jwt_bp.name)
docs.register(UsersResource, blueprint=jwt_bp.name)