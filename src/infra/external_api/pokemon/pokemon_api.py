from typing import List
from extensions.logger import get_logger
from infra.external_api.base.base_api import BaseAPI, MethodType
from infra.external_api.pokemon.model.pokemon import Pokemon
from infra.external_api.pokemon.model.pagedResponse_pokemon import PagedResponse_Pokemons
from infra.external_api.pokemon.model.type_pokemon import TypePokemon


logger = get_logger(__name__)

class PokemonAPI(BaseAPI):
    def __init__(self, url):
        super().__init__(url)
        self._lock = object()

    # Method to get type of pokemon
    async def get_type(self, type_name) -> TypePokemon:
        try:
            logger.info(f"Init {__name__}")

            url = f"/type/{type_name}"

            type = await self.call_api(MethodType.GET, url, TypePokemon)

            return type
        except Exception as e:
            logger.error(f"Error {__name__}")
            raise e
        finally:
            logger.info(f"Error {__name__}")

    
    # Method to get pokemon
    async def get_pokemon(self, name) -> Pokemon:
        try:
            logger.info(f"Init {__name__}")

            url = f"/pokemon/{name}"

            pokemon = await self.call_api(MethodType.GET, url, response_type=Pokemon)

            return pokemon
        except Exception as e:
            logger.error(f"Error {__name__}")
            raise e
        finally:
            logger.info(f"End {__name__}")
    
    # Method to get paged pokemons
    async def get_paged_pokemon(self, offset, limit) -> PagedResponse_Pokemons:
        try:
            logger.info(f"Init {__name__}")

            url = f"/pokemon"

            pokemon = await self.call_api(MethodType.GET, url, None, {"offset" : offset, "limit": limit }, response_type=PagedResponse_Pokemons)

            return pokemon
        except Exception as e:
            logger.error(f"Error {__name__}")
            raise e
        finally:
            logger.info(f"End {__name__}")
