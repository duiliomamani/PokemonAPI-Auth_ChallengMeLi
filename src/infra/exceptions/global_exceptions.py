from typing import List, Optional

class BaseException(Exception):
    """Custom Error Exception"""

    def __init__(
        self,
        code: Optional[int],
        description: Optional[str],
        errors: Optional[List[dict]]
    ) -> None:
        super().__init__()
        self.code = code if code is not None else 400
        self.description = (
            description
            if description is not None
            else "One or more errors have occurred."
        )
        self.errors = errors


class BusinessExceptionError(BaseException):
    def __init__(self, errors: Optional[List[dict]]) -> None:
        super().__init__(
            code=400, description="One or more errors have occurred.", errors=errors
        )


class ValidationExceptionError(BaseException):
    def __init__(self, errors: Optional[List[dict]]) -> None:
        super().__init__(
            code=400, description="One or more errors have occurred.", errors=errors
        )


class InternalExceptionError(BaseException):
    def __init__(self, errors: Optional[List[dict]]) -> None:
        super().__init__(
            code=500,
            description="We were unable to process your request. We are unable to perform the requested operation at this time.",
            errors=errors,
        )
