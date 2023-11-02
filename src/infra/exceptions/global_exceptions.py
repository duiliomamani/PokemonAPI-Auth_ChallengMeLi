from typing import List, Optional


class BaseException(Exception):
    """Custom Error Exception"""

    def __init__(
        self,
        code: Optional[int],
        description: Optional[str],
        errors: Optional[List[dict]],
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
    def __init__(self, errors: Optional[List[dict]] = None) -> None:
        super().__init__(
            code=400, description="One or more errors have occurred.", errors=errors
        )


class ValidationExceptionError(BaseException):
    def __init__(self, errors: Optional[List[dict]] = None) -> None:
        super().__init__(
            code=400, description="One or more errors have occurred.", errors=errors
        )


class UnauthorizedExceptionError(BaseException):
    def __init__(self, errors: Optional[List[dict]] = None) -> None:
        super().__init__(
            code=401,
            description="Not authenticated to access the URL requested.",
            errors=errors,
        )


class ForbiddenExceptionError(BaseException):
    def __init__(self, errors: Optional[List[dict]] = None) -> None:
        super().__init__(
            code=403,
            description="Not authorized to access the URL requested.",
            errors=errors,
        )
