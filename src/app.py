from flask import Flask
from extensions.routes import register_routes
from extensions.exceptions import register_exception_handler

def create_app():
    app = Flask(__name__)
    # will move to register_config soon
    app.config["ERROR_404_HELP"] = False
    register_routes(app)
    register_exception_handler(app)


    return app
