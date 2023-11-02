from functools import wraps
from flask import make_response, request
from api.interactor.dtos._base.tresponse_dto import TResponse
from api.controllers._base._base_controlles import jsonify_custom

from core.services.auth.auth_services import AuthServices
from extensions.logger import get_logger
from infra.exceptions.global_exceptions import BaseException

logger = get_logger(__name__)

def require_appkey(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            header = request.headers.environ.get("HTTP_X_API_KEY")
            is_authenticed = AuthServices.is_authenticed(api_key=header)
            if is_authenticed[0]:
                path = request.url_rule.rule
                method = request.method
                is_authorized = AuthServices.is_authorized(
                    client=is_authenticed[1], method=method, permission=path
                )
                if is_authorized:
                    return f(*args, **kwargs)
        except BaseException as e:
            return make_response(jsonify_custom( TResponse(False, e.description, e.errors or [])), e.code)

    return wrapper
