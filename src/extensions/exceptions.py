from flask import Flask
from werkzeug.exceptions import HTTPException
from api.controllers._base._base_controlles import jsonify_custom
from extensions.logger import get_logger
from infra.exceptions.global_exceptions import BaseException
from api.interactor.dtos._base.tresponse_dto import TResponse

logger = get_logger(__name__)


def handle_base_exception_error(e: BaseException):
    """Make JSON Error Response instead of Web Page"""

    rsp = TResponse(False, e.description, e.errors or [])

    logger.error(f"Description: {rsp.message}")
    logger.error(f"Errors: {rsp.errors}")
    return jsonify_custom(rsp), e.code

def handle_global_error(e: Exception):
    """Make JSON Error Response instead of Web Page"""
    logger.error(f"HandlerGLOBAL: {e.args}")

    rsp = TResponse(False, e.__class__.__name__, [e.args])

    logger.error(f"Description: {rsp.message}")
    logger.error(f"Errors: {rsp.errors}")
    return jsonify_custom(rsp), 500


def register_exception_handler(app: Flask):
    app.register_error_handler(BaseException, handle_base_exception_error)
    app.register_error_handler(Exception, handle_global_error)
