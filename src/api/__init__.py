from flask import Blueprint, jsonify
from extensions.logger import get_logger

from api.interactor.dtos._base.tresponse_dto import TResponse
from api.controllers._base._base_controlles import jsonify_custom
from infra.exceptions.global_exceptions import BaseException

api_bp = Blueprint("_api_challenge", __name__, url_prefix="/api")

logger = get_logger(__name__)


# Decorador para manejar excepciones personalizadas
@api_bp.errorhandler(BaseException)
def handle_custom_exception(e: BaseException):
    """Make JSON Error Response instead of Web Page"""

    rsp = TResponse(False, e.description, e.errors or [])

    logger.error(f"{e.description}: {rsp['message']}")
    logger.error(f"{e.erros}: {rsp['errors']}")
    return jsonify_custom(rsp), e.code
