from core.domain.clients import Client, clients_mock
from extensions.logger import get_logger
from infra.exceptions.global_exceptions import (
    UnauthorizedExceptionError,
    ForbiddenExceptionError,
)

logger = get_logger(__name__)


class AuthServices:
    @classmethod
    def is_authenticed(self, api_key: str):
        try:
            logger.info(f"Init {__name__}")

            # ToDo Access DataBase Mongo
            # Get client by ApiKey
            client = next(filter(lambda x: x.api_key == api_key, clients_mock), None)

            if client is None:
                raise UnauthorizedExceptionError

            return True, client
        except Exception as e:
            logger.error(f"Error {__name__}")
            raise e
        finally:
            logger.info(f"End {__name__}")

    @classmethod
    def is_authorized(self, client: Client, permission: str, method: str) -> bool:
        try:
            logger.info(f"Init {__name__}")

            # Verify if client has access to resource with action
            permission = next(
                filter(
                    lambda x: x.resource == permission and x.method == method,
                    client.permission,
                ),
                None,
            )
            if permission is None:
                raise ForbiddenExceptionError

            return True
        except Exception as e:
            logger.error(f"Error {__name__}")
            raise e
        finally:
            logger.info(f"End {__name__}")
