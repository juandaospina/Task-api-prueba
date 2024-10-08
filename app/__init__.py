from flask import Flask
from flask_restful import Api
from flask_apispec.extension import APISpec, MarshmallowPlugin
from flask_jwt_extended import JWTManager

from .db import db, ma, migrate
from app.docs import docs
from app.auth.router import jwt_bp 
from app.todos.router import tasks_bp
from app.errors_handling import register_errors


def initialize_extensions(app: Flask):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    docs.init_app(app)
    jwt = JWTManager()
    jwt.init_app(app)


def configure_docs(app: Flask):
    spec = APISpec(
        title='Todos API',
        version='1.0',
        openapi_version="2.0", 
        plugins=[MarshmallowPlugin()],
    )
    api_key_scheme = {"type": "apiKey", "scheme": "Bearer", 
                      "in": "header", "name": "Authorization", 
                      "description": "You must manually prefix your API token with Bearer like Bearer <token>"}
    spec.components.security_scheme("Bearer", api_key_scheme)
    app.config.update({
        "APISPEC_SPEC": spec,
        'APISPEC_SWAGGER_URL': '/docs',
        'APISPEC_SWAGGER_UI_URL': '/docs-ui',
    })


def register_blueprints(app: Flask):
    app.register_blueprint(tasks_bp)
    app.register_blueprint(jwt_bp)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Config
    app.config.from_object("app.config")
    app.config.from_pyfile("config.py", silent=True)

    Api(app, catch_all_404s=False)

    # Blueprints
    register_blueprints(app)

    # Documentation
    configure_docs(app)

    # Error handling
    register_errors(app)

    # Extensions
    initialize_extensions(app)

    return app