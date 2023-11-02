from dataclasses import dataclass
from typing import List


@dataclass
class Resource:
    resource: str
    method: str


@dataclass
class Client:
    name: str
    api_key: str
    permission: List[Resource]


# Mock Clients Authorized
clients_mock: List[Client] = [
    Client(
        name="client_MeLi_IAM",
        api_key="NzNjMmEwY2QtMGE1YS00NTJhLTk5MTEtNjAwNGJlYWQ3Nzlk",
        permission=[
            Resource("/api/pokemon/<string:name>", "GET"),
            Resource("/api/pokemon/random/type/<string:type_name>", "GET"),
            Resource("/api/pokemon/max-length/type/<string:type_name>", "GET"),
            Resource("/api/pokemon", "GET"),
        ],
    ),
    Client(
        name="client_Company_IAM",
        api_key="OGNmOGIzNWYtNjZhNS00NjE4LTk0ZWItODk3MDc5ZDY3ZmZl",
        permission=[],
    ),
    Client(
        name="client_TechCode_IAM",
        api_key="N2UwOWVlMzAtMzViMi00Nzk5LWE2MzktZGUwZGY0MDgyZjky",
        permission=[
            Resource("/api/pokemon", "GET"),
        ],
    ),
    Client(
        name="client_Avenger_IAM",
        api_key="ZTIzZWU5NWEtZTM5Ny00NzNlLThlY2ItNTRlNWFlYWIzNmVl",
        permission=[
            Resource("/api/pokemon/random/type/<string:type_name>", "GET"),
            Resource("/api/pokemon/max-length/type/<string:type_name>", "GET"),
        ],
    ),
    Client(
        name="client_Pokedex_IAM",
        api_key="YzMzYjU5YzUtY2ZjYy00NzdlLWJkMmMtNjEwNGI1ZWVkYTI1",
        permission=[
            Resource("/api/pokemon/<string:name>", "GET"),
            Resource("/api/pokemon", "GET"),
        ],
    ),
]
