import asyncio
from flask_restx import Resource, reqparse
from injector import inject
from api.controllers._base._base_controlles import jsonify_custom, auth
from api.interactor.dtos._base.tresponse_dto import TResponse
from api.interactor.dtos.pokemon_dto import pokemon_ns as ns
from api.interactor.dtos.pokemon_dto import pokemon_model_response, response
from core.services.pokemon.pokemon_services import PokemonServices


@ns.route(
    "/<string:name>",
    methods=["GET"],
    doc={"description": "Get Pokemon by name"},
)
@ns.doc(params={"name": "A name of pokemon"})
@ns.response(200, "Success", pokemon_model_response)
@ns.response(400, "Bad Request", response)
@ns.response(401, "Unauthorized", response)
@ns.response(403, "Forbidden", response)
@ns.response(500, "Internal Server Error", response)
class Pokemon(Resource):
    @inject
    def __init__(self, svc: PokemonServices, **kwargs):
        self.svc = svc
        # Don't know if really needed
        super().__init__(**kwargs)

    @auth
    def get(self, name: str):
        data = asyncio.run(self.svc.get_pokemon(name))

        response = TResponse(data=data)

        return jsonify_custom(response)


@ns.route(
    "/random/type/<string:type_name>",
    methods=["GET"],
    doc={"description": "Get a pokemon random by type name"},
)
@ns.doc(params={"type_name": "A type name of pokemon"})
@ns.response(200, "Success", pokemon_model_response)
@ns.response(400, "Bad Request", response)
@ns.response(401, "Unauthorized", response)
@ns.response(403, "Forbidden", response)
@ns.response(500, "Internal Server Error", response)
class PokemonRandomType(Resource):
    @inject
    def __init__(self, svc: PokemonServices, **kwargs):
        self.svc = svc
        # Don't know if really needed
        super().__init__(**kwargs)

    @auth
    @ns.response(200, "Success", pokemon_model_response)
    def get(self, type_name: str):
        response = asyncio.run(self.svc.get_random_pokemon_by_type(type_name))
        return jsonify_custom(response)


@ns.route(
    "/max-length/type/<string:type_name>",
    methods=["GET"],
    doc={
        "description": "Get multiple Pokémon named by maximum length and by type name"
    },
)
@ns.doc(params={"type_name": "A type name of pokemon"})
@ns.response(200, "Success", pokemon_model_response)
@ns.response(400, "Bad Request", response)
@ns.response(401, "Unauthorized", response)
@ns.response(403, "Forbidden", response)
@ns.response(500, "Internal Server Error", response)
class PokemonRandomType(Resource):
    @inject
    def __init__(self, svc: PokemonServices, **kwargs):
        self.svc = svc
        # Don't know if really needed
        super().__init__(**kwargs)

    @auth
    def get(self, type_name: str):
        response = asyncio.run(self.svc.get_max_length_name_pokemons(type_name))

        return jsonify_custom(response)


parser = reqparse.RequestParser()
parser.add_argument(
    "filter", action="split", required=True, help="Filter by char in name"
)
parser.add_argument(
    "latitude", type=float, required=True, help="Current location latitude geocode"
)
parser.add_argument(
    "longitude", type=float, required=True, help="Current location longitude geocode"
)


@ns.route(
    "",
    methods=["GET"],
    doc={
        "description": "Get a random pokemon by the strongest type in the current climate by coordinates"
    },
)
@ns.doc(params={"filter": "A name of pokemon"})
@ns.doc(params={"latitude": "Current location latitude geocode"})
@ns.doc(params={"longitude": "Current location longitude geocode"})

@ns.response(200, "Success", pokemon_model_response)
@ns.response(400, "Bad Request", response)
@ns.response(401, "Unauthorized", response)
@ns.response(403, "Forbidden", response)
@ns.response(500, "Internal Server Error", response)
class PokemonRandomType(Resource):
    @inject
    def __init__(
        self, svc: PokemonServices, **kwargs
    ):  # <- here just added **kwargs to receice the extra passed `api` parameter
        self.svc = svc
        # Don't know if really needed
        super().__init__(**kwargs)

    @auth
    def get(self):
        args = parser.parse_args()

        response = asyncio.run(
            self.svc.get_pokemon_by_filter_with_weather(
                args["filter"], args["latitude"], args["longitude"]
            )
        )

        return jsonify_custom(response)
