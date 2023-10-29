from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TypePokemon:
    id: Optional[int] = None
    name: str = ''
    url: Optional[str] = ''
    pokemons: Optional[List['Pokemon']] = None

    def to_class(payload):
        from infra.external_api.pokemon.model.pokemon import Pokemon
        pokemons_data = payload.get("pokemon", [])
        pokemons = [Pokemon.to_class(data.get("pokemon")) for data in pokemons_data]
        return TypePokemon(
            payload.get("id", None),
            payload.get("name", ""),
            payload.get("url", ""),
            pokemons
        )
