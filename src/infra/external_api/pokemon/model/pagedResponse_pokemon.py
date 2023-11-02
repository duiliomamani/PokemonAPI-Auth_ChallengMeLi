from dataclasses import dataclass
from typing import List, Optional


@dataclass
class PagedResponse_Pokemons:
    count: Optional[int]
    next: Optional[str]
    previous: Optional[str]
    results: Optional[List["Pokemon"]]

    def to_class(payload):
        from infra.external_api.pokemon.model.pokemon import Pokemon

        results = payload.get("results", [])
        results = [Pokemon.to_class(data) for data in results]
        return PagedResponse_Pokemons(
            payload.get("count", None),
            payload.get("next", None),
            payload.get("previous", None),
            results
        )
