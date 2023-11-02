import random
from infra.external_api.pokemon.pokemon_api import PokemonAPI
from infra.external_api.weatherforecast.weatherforecast_api import WeatherForecastAPI
from core.domain.weatherforecast_types import get_weather_type

api = PokemonAPI()
api_weahter = WeatherForecastAPI()


class PokemonServices:
    @classmethod
    async def get_pokemon(self, name: str):
        try:
            pokemon = await api.get_pokemon(name)

            return pokemon
        except Exception as e:
            raise e

    @classmethod
    async def get_pokemon_by_types(self, type_name: str):
        try:
            type = await api.get_type(type_name)

            return type.pokemons
        except Exception as e:
            raise e
        
    @classmethod
    async def get_random_pokemon_by_type(self, type_name: str):
        try:
            pokemons = await self.get_pokemon_by_types(type_name)

            poke_random = random.choice(pokemons)

            pokemon = await self.get_pokemon(name=poke_random.name)

            return pokemon
        except Exception as e:
            raise e

    @classmethod
    async def get_max_length_name_pokemons(self, type_name: str):
        try:
            pokemons = await self.get_pokemon_by_types(type_name)

            max_len = len(max(pokemons, key=lambda x: len(x.name)).name)
            pokemons_name_max_len = [i for i in pokemons if len(i.name) == max_len]

            pokemons = []

            for p in pokemons_name_max_len:
                pokemons.append(await self.get_pokemon(name=p.name))

            return pokemons
        except Exception as e:
            raise e

    @classmethod
    async def get_pokemon_by_filter_with_weather(self, filter_characters, latitude, longitude):
        try:
            current_weather = await api_weahter.get_actual_temperature_by_location(latitude, longitude)

            type_strong = get_weather_type(current_weather.current.temperature)

            pokemons = await self.get_pokemon_by_types(type_strong)
            
            filter = [objeto for objeto in pokemons if any(char in objeto.name for char in filter_characters)]

            poke_random = random.choice(filter)

            pokemon = await self.get_pokemon(poke_random.name)

            return pokemon
        except Exception as e:
            raise e

    @classmethod
    async def get_all_pokemons(self):
        try:
            limit = 100
            offset = 0

            paged = await api.get_paged_pokemon(offset=offset, limit=limit)
            pokemons = []

            while paged.next is not None:
                pokemons = paged.results + pokemons
                limit += 100
                offset += 100
                paged = await api.get_paged_pokemon(offset=offset, limit=limit)

            return pokemons
        except Exception as e:
            raise e
