import random
from infra.external_api.pokemon.pokemon_api import PokemonAPI

api = PokemonAPI()

class PokemonServices:
    @classmethod
    async def get_pokemon(self, name: str):
        return await api.get_pokemon(name)

    @classmethod
    async def get_random_pokemon_by_type(self, type_name: str):
        type = await api.get_type(type_name)

        poke_random = random.choice(type.pokemons)

        pokemon = await self.get_pokemon(name=poke_random.name)

        return pokemon

    @classmethod
    async def get_max_length_name_pokemons(self, type_name: str):
        type = await api.get_type(type_name)

        max_len = len(max(type.pokemons, key=lambda x: len(x.name)).name)
        pokemons_name_max_len = [i for i in type.pokemons if len(i.name) == max_len]

        pokemons = []

        for p in pokemons_name_max_len:
            pokemons.append(await self.get_pokemon(name=p.name))

        return pokemons