import re
import requests
from typing import Type, TypeVar
from enum import Enum
from dataclasses import dataclass
from flask import json
from extensions.logger import get_logger

from infra.exceptions.global_exceptions import BaseException

logger = get_logger(__name__)


class MethodType(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"


T = TypeVar("T")


@dataclass
class DynamicPayload:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def from_dict_to_instance(cls: Type[T], data: dict) -> T:
        return cls.to_class(data)


class BaseAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.headers = {}

    async def call_api(
        self,
        type_method: MethodType,
        resource: str,
        response_type: Type[T],
        data=None,
        parameters=None,
        headers=None,
    ) -> T:
        try:
            parameters_parsed = ""
            data_convert = None
            response_http = None

            # Mappint headers to request header
            if headers:
                for h, hv in headers.items():
                    self.headers[h] = hv

            # Mapping parameters for request query string
            if parameters:
                parameters_parsed = "&".join(
                    [
                        f"{item}={value}"
                        for item, value in parameters.items()
                        if value is not None
                    ]
                )
                if parameters_parsed:
                    parameters_parsed = "?" + parameters_parsed

            # Mapping data for request body
            if data:
                json_data = json.dumps(data)
                data_convert = json.loads(json_data)

            url = f"{self.base_url}{resource}{parameters_parsed}"

            if type_method == MethodType.GET:
                response_http = requests.get(url, headers=self.headers)
            elif type_method == MethodType.PUT:
                response_http = requests.put(
                    url, json=data_convert, headers=self.headers
                )
            elif type_method == MethodType.POST:
                response_http = requests.post(
                    url, json=data_convert, headers=self.headers
                )
            elif type_method == MethodType.DELETE:
                response_http = requests.delete(url, headers=self.headers)

            status_code = response_http.status_code

            if status_code == 200:
                string_result = response_http.text
                string_result = re.sub(r"[{]+\s+[}]|[{]+[}]", "null", string_result)
                # Convert string_result to response_type
                response = DynamicPayload.from_dict_to_instance(
                    response_type, data=json.loads(string_result)
                )

                log = (
                    f"ApiBase | {url} |{type_method} | {status_code} | {string_result}"
                )
                logger.info(log)
            else:
                raise BaseException(status_code, "One or more errors have occurred when call api.", None )

            return response
        except Exception as e:
            string_result = response_http.text
            log = f"ApiBase | {url} | {type_method} | {status_code} | {string_result}"
            logger.info(log)
            raise e
