from flask import Flask
from api.controllers._base._base_controlles import jsonify_custom
from extensions.logger import get_logger
from infra.exceptions.global_exceptions import BaseException
from api.interactor.dtos._base.tresponse_dto import TResponse

logger = get_logger(__name__)


def handle_global_error(e: BaseException):
    """Make JSON Error Response instead of Web Page"""

    rsp = TResponse(False, e.description, e.errors or [])

    logger.error(f"{e.description}: {rsp.message}")
    logger.error(f"{e.errors}: {rsp.errors}")
    return jsonify_custom(rsp), e.code


def register_exception_handler(app: Flask):
    app.register_error_handler(BaseException, handle_global_error)
