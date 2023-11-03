from flask_restx import  Namespace, fields
from api.interactor.dtos._base.tresponse_dto import tresponse_model

pokemon_ns = Namespace("Pokemon", description="Pokemon Endpoints")

response = pokemon_ns.model("Response", model=tresponse_model)

type_pokemon_model = pokemon_ns.model(
    "TypePokemon",
    {"id": fields.Integer, "name": fields.String, "url": fields.String},
)

type_pokemon_response = pokemon_ns.inherit(
    "TypePokemonResponse",
    response,
    {"data": fields.Nested(type_pokemon_model)},
)

pokemon_model = pokemon_ns.model(
    "Pokemon",
    {
        "id": fields.Integer,
        "name": fields.String,
        "url": fields.String,
        "types": fields.Nested(type_pokemon_model),
    },
)

pokemon_model_response = pokemon_ns.inherit(
    "PokemonReponse",
    response,
    {"data": fields.Nested(pokemon_model)},
)
