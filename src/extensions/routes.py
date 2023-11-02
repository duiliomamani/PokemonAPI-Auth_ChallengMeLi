
from flask import Flask
from api import api_pk, api as api_definition

from flask_restx import Api

from api.controllers.pokemon.pokemon_controller import ns as pokemon_ns

def register_routes(app: Flask):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(api_pk)