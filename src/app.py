from flask import Flask
from extensions.injector import register_dependency_injection
from extensions.routes import register_routes
from extensions.exceptions import register_exception_handler

from config import configurations

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configurations[config_name])

    register_routes(app)
    register_dependency_injection(app)
    register_exception_handler(app)

    return app
