from typing import List
from infra.external_api.base.base_api import BaseAPI, MethodType
from infra.external_api.pokemon.model.pokemon import Pokemon
from infra.external_api.pokemon.model.pagedResponse_pokemon import PagedResponse_Pokemons
from infra.external_api.pokemon.model.type_pokemon import TypePokemon


class PokemonAPI(BaseAPI):
    def __init__(self):
        super().__init__("https://pokeapi.co/api/v2")
        self._lock = object()

    async def get_type(self, type_name) -> TypePokemon:
        url = f"/type/{type_name}"

        type = await self.call_api(MethodType.GET, url, TypePokemon)

        return type

    async def get_pokemon(self, name) -> Pokemon:
        url = f"/pokemon/{name}"

        pokemon = await self.call_api(MethodType.GET, url, response_type=Pokemon)

        return pokemon
    
    async def get_paged_pokemon(self, offset, limit) -> PagedResponse_Pokemons:
        url = f"/pokemon?offset={offset}&limit={limit}"

        pokemon = await self.call_api(MethodType.GET, url, response_type=PagedResponse_Pokemons)

        return pokemon
