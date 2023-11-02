
from flask import Flask
from api import api_pk

def register_routes(app: Flask):
    """
    Register routes with blueprint and namespace
    """
    app.register_blueprint(api_pk)