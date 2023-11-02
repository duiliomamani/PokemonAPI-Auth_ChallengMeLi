from flask import Blueprint
from flask_restx import Api
from extensions.logger import get_logger

from api.interactor.dtos._base.tresponse_dto import TResponse
from api.controllers._base._base_controlles import jsonify_custom
from api.controllers.pokemon.pokemon_controller import ns as pokemon_ns

api_pk = Blueprint("apichallenge", __name__, url_prefix="/api")

logger = get_logger(__name__)

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "X-API-KEY"}}

api = Api(
    api_pk,
    doc="/docs",
    title="Challenge MeLI - PokeWeather API",
    version="1.0",
    description="MercadoLibre Challenge: Weather for Pokémons",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(pokemon_ns, path="/pokemon")
