from flask_restx import Namespace, fields

pokemon_ns = Namespace("Pokemon_Ns", description="Pokemon Endpoints")

type_pokemon = pokemon_ns.model(
    "TypePokemon",
    {
        "id": fields.Integer,
        "name": fields.String,
        "url": fields.String
    },
)

pokemon_model = pokemon_ns.model(
    "Pokemon",
    {
        "id": fields.Integer,
        "name": fields.String,
        "url": fields.String,
        "types": fields.Nested(type_pokemon)
    }
)
