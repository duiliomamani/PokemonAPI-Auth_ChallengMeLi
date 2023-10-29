from flask import Flask
from flask_restx import Api

from api.controllers.pokemon.pokemon_controller import ns as pokemon_ns
from extensions.routes import register_routes
from extensions.exceptions import register_exception_handler

def create_app():
    app = Flask(__name__)
    # will move to register_config soon
    app.config["ERROR_404_HELP"] = False

    api = Api(
        app,
        title="Resource API",
        version="1.0",
        description="A description",
    )

    api.add_namespace(pokemon_ns, "/pokemon")

    register_routes(app)
    register_exception_handler(app)


    return app
