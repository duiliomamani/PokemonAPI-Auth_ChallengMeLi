
from flask import Flask
from api import api_bp as api

def register_routes(app: Flask):
    """
    Register routes with blueprint and namespace
    """
    
    app.register_blueprint(api)