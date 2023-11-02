from typing import List, Optional

from flask_restx import Model, fields

tresponse_model = Model(
    "Reponse",
    {
        "errors": fields.List(fields.String),
        "message": fields.String,
        "is_successfull": fields.Boolean,
    },
)


class TResponse:
    is_successfull: Optional[bool] = True
    message: Optional[str] = ""
    errors: Optional[List] = []
    data: Optional[dict]

    def __init__(
        self,
        is_successfull=True,
        message=None,
        errors=None,
        data: Optional[dict] = None,
    ) -> None:
        self.is_successfull = is_successfull
        self.message = message
        self.errors = errors
        self.data = data
