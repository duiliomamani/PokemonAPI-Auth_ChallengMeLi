import asyncio
from functools import wraps
from flask import request, abort
from core.services.auth.auth_services import AuthServices

def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        header =request.headers.environ.get('HTTP_X_API_KEY')
        #Validate ToDo API-KEY
        path =request.url_rule.rule
        method =request.method
        is_authorized= asyncio.run(AuthServices.is_authorized(api_key=header, permission=path, method=method))
        if is_authorized:
            return view_function(*args, **kwargs)
    return decorated_function