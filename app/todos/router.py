from flask import Blueprint
from flask_restful import Api, Resource
from flask_apispec import views, doc, marshal_with, use_kwargs
from flask_jwt_extended import jwt_required

from .schemas import TaskPOSTSchema, TaskSchema, TaskPUTSchema
from . import repository
from app.docs import docs
from app.common import ResponseSchema


tasks_bp = Blueprint('tasks', __name__, url_prefix="/v1")
api = Api(tasks_bp)
    

@doc(tags=['Tasks'], security=[{"Bearer": []}])
class BooksResource(views.MethodResource, Resource):
    @doc(description="Get all tasks from database")
    @marshal_with(TaskSchema(many=True), code=200)
    @jwt_required()
    def get(self):
        tasks = repository.get_tasks()
        return tasks, 200

    @doc(description="Create a new book in the repository", code=200, 
         security=[{"Bearer": []}], 
         responses={
             404: {'description': 'Objecto no encontrado.'},
             422: {'description': 'Entidad no procesable.'}
         })
    @marshal_with(ResponseSchema, code=200)
    @use_kwargs(TaskPOSTSchema, location="json")
    @jwt_required()
    def post(self, **kwargs):
        repository.create_task(**kwargs)
        return ResponseSchema().load(
            {'message': '¡Tarea creada exitosamente!'}), 200
    

@doc(tags=["Tasks"], security=[{"Bearer": []}])
class TaskResource(views.MethodResource, Resource):
    @doc('Actualiza una tarea.')
    @marshal_with(ResponseSchema, code=200)
    @use_kwargs(TaskPUTSchema, location='json')
    @jwt_required()
    def put(self, task_id: int, **kwargs):
        repository.update_task(task_id, **kwargs)
        return ResponseSchema().load(
            {'message': '¡Tarea editada existosamente!'}), 200


# Add resources
api.add_resource(BooksResource, "/tasks")
api.add_resource(TaskResource, "/tasks/<int:task_id>")
# Register resources for docs
docs.register(BooksResource, blueprint=tasks_bp.name)
docs.register(TaskResource, blueprint=tasks_bp.name)