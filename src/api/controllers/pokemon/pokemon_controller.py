import asyncio
from flask_restx import Resource, reqparse
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
class Pokemon(Resource):
    @ns.response(200, "Success", pokemon_model_response)
    @ns.response(400, "Bad Request", response)
    @ns.response(500, "Internal Server Error", response)
    @auth
    def get(self, name: str):
        data = asyncio.run(PokemonServices.get_pokemon(name))

        response = TResponse(data=data)

        return jsonify_custom(response)


@ns.route(
    "/random/type/<string:type_name>",
    methods=["GET"],
    doc={"description": "Get a pokemon random by type name"},
)
@ns.doc(params={"type_name": "A type name of pokemon"})
class PokemonRandomType(Resource):
    @ns.response(200, "Success", pokemon_model_response)
    @ns.response(400, "Bad Request", response)
    @ns.response(500, "Internal Server Error", response)
    @auth
    def get(self, type_name: str):
        response = asyncio.run(PokemonServices.get_random_pokemon_by_type(type_name))
        return jsonify_custom(response)


@ns.route(
    "/max-length/type/<string:type_name>",
    methods=["GET"],
    doc={"description": "Get multiple Pokémon named by maximum length and by type name"},
)
@ns.doc(params={"type_name": "A type name of pokemon"})
class PokemonRandomType(Resource):
    @ns.response(200, "Success", pokemon_model_response)
    @ns.response(400, "Bad Request", response)
    @ns.response(500, "Internal Server Error", response)
    @auth
    def get(self, type_name: str):
        response = asyncio.run(PokemonServices.get_max_length_name_pokemons(type_name))

        return jsonify_custom(response)


parser = reqparse.RequestParser()
parser.add_argument("filter", action="split", required=True, help="Filter by char in name")
parser.add_argument("latitude", type=float, required=True, help="Current location latitude geocode")
parser.add_argument("longitude",  type=float, required=True, help="Current location longitude geocode")

@ns.route(  
    "",
    methods=["GET"],
    doc={"description": "Get a random pokemon by the strongest type in the current climate by coordinates"},
)
@ns.doc(params={"filter": "A name of pokemon"})
@ns.doc(params={"latitude": "Current location latitude geocode"})
@ns.doc(params={"longitude": "Current location longitude geocode"})
class PokemonRandomType(Resource):
    @ns.response(200, "Success", pokemon_model_response)
    @ns.response(400, "Bad Request", response)
    @ns.response(500, "Internal Server Error", response)
    @auth
    def get(self):
        args = parser.parse_args()

        response = asyncio.run(PokemonServices.get_pokemon_by_filter_with_weather(args["filter"], args["latitude"], args["longitude"]))
        
        return jsonify_custom(response)