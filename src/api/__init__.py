from http.client import HTTPException

from flask import Blueprint, jsonify
from flask_restx import Api


api_bp = Blueprint("_api_challenge", __name__, url_prefix="/api")

@api_bp.errorhandler(HTTPException)
def handle_error(error: HTTPException):
    """Handle BluePrint JSON Error Response"""
    response = {
        "error": error.__class__.__name__,
        "message": error.description,
    }
    return response, error.code
