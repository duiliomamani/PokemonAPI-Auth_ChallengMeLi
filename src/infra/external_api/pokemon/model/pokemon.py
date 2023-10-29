from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Pokemon:
    id: Optional[int]
    name: str
    url: Optional[str]
    base_experience: Optional[int]
    height: Optional[int]
    is_default: Optional[bool]
    order: Optional[int]
    weight: Optional[int]
    types: Optional[List['TypePokemon']]

    def to_class(payload):
        from infra.external_api.pokemon.model.type_pokemon import TypePokemon

        types_data = payload.get("types", [])
        types = [TypePokemon.to_class(data.get("type")) for data in types_data]

        return Pokemon(
            payload.get("id", None),
            payload.get("name", None),
            payload.get("url", None),
            payload.get("base_experience", None),
            payload.get("height", None),
            payload.get("is_default", None),
            payload.get("order", None),
            payload.get("weight", None),
            types,
        )
