import re
import requests
from typing import Optional, Type, TypeVar
from enum import Enum
from dataclasses import dataclass
from flask import json

from infra.exceptions.global_exceptions import (
    BaseException,
)


class MethodType(Enum):
    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    DELETE = "DELETE"


@dataclass
class ApiParameter:
    Name: str
    Value: Optional[str]


T = TypeVar("T")


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
        parameters_parsed = ""
        data_convert = None
        response_http = None

        if headers:
            for h in headers:
                self.headers[h.Name] = h.Value

        if parameters:
            parameters_parsed = "&".join(
                [
                    f"{item.Name}={item.Value}"
                    for item in parameters
                    if item.Value is not None
                ]
            )
            if parameters_parsed:
                parameters_parsed = "?" + parameters_parsed

        if data:
            json_data = json.dumps(data)
            data_convert = json.loads(json_data)

        url = f"{self.base_url}/{resource}{parameters_parsed}"

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
            response = DynamicPayload.from_dict_to_instance(
                response_type, data=json.loads(string_result)
            )
        else:
            log = f"ApiBase | {type_method} | {status_code}"
            string_result = response_http.text
            raise BaseException(
                status_code, "One or more errors have occurred when call api."
            )

        return response
