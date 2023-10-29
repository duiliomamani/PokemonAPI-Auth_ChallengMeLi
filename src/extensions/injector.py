# from flask_injector import FlaskInjector
# from injector import singleton, scoped, transient, Binder

# from ..infra.external_api.pokemon.pokemon_api import PokemonAPI


# def configure_binding(binder: Binder) -> Binder:
#     binder.bind(PokemonAPI, to=PokemonAPI, scope=singleton)
#     return binder


# def register_dependency_injection(app):
#     FlaskInjector(app=app, modules=[configure_binding])
