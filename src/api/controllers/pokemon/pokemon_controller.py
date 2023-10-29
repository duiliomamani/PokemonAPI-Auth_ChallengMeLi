import asyncio
from flask_restx import Resource
from api.controllers._base._base_controlles import jsonify_custom
from api.interactor.dtos.pokemon_dto import pokemon_ns as ns
from api.interactor.dtos.pokemon_dto import pokemon_model
from core.services.pokemon.pokemon_services import PokemonServices


@ns.route("/<string:name>", methods=["GET"], endpoint="/")
@ns.doc("Get Pokemon by Name", params={"name": "A name of pokemon"})
class Pokemon(Resource):
    @ns.response(200, "Success", pokemon_model)
    def get(self, name: str):
        response = asyncio.run(PokemonServices.get_pokemon(name))

        if response:
            return jsonify_custom(response)
        else:
            return jsonify_custom({"error": "Pokemon not found"}), 404


@ns.route("/random/type/<string:type_name>", methods=["GET"])
@ns.doc(params={"type_name": "A type name of pokemon"})
class PokemonRandomType(Resource):
    @ns.response(200, "Success", pokemon_model)
    def get(self, type_name: str):
        response = asyncio.run(PokemonServices.get_random_pokemon_by_type(type_name))

        if response:
            return jsonify_custom(response)
        else:
            return jsonify_custom({"error": "Pokemon not found"}), 404


@ns.route("/max-length/type/<string:type_name>", methods=["GET"])
@ns.doc(params={"type_name": "A type name of pokemon"})
class PokemonRandomType(Resource):
    @ns.response(200, "Success", pokemon_model)
    def get(self, type_name: str):
        response = asyncio.run(PokemonServices.get_max_length_name_pokemons(type_name))

        if response:
            return jsonify_custom(response)
        else:
            return jsonify_custom({"error": "Pokemon not found"}), 404


@ns.route("/hello", methods=["GET"])
class PokemonHelloResource(Resource):
    @ns.doc("hello")
    def get(self):
        return "Hello from Home Page"
