from flask_injector import FlaskInjector
from injector import Injector, Module, singleton, Binder
from core.services.pokemon.pokemon_services import PokemonServices

from infra.external_api.pokemon.pokemon_api import PokemonAPI
from infra.external_api.weatherforecast.weatherforecast_api import WeatherForecastAPI

class AppModule(Module):
    def __init__(self, app):
        self.app = app

    """Configure the application."""
    def configure(self, binder: Binder):
        binder.bind(PokemonAPI, to=self.configure_pokemon_api(), scope=singleton)
        binder.bind(WeatherForecastAPI, to=self.configure_weather_api(), scope=singleton)
        binder.bind(PokemonServices, to=PokemonServices, scope=singleton)

    def configure_pokemon_api(self) -> PokemonAPI:
        return PokemonAPI(
            url=self.app.config.get('POKE_API')
        )
    def configure_weather_api(self) -> WeatherForecastAPI:
        return WeatherForecastAPI(
            url=self.app.config.get('WEATHER_API')
        )

def register_dependency_injection(app):
    # Inject Services for all application
    injector = Injector([AppModule(app)])
    FlaskInjector(app=app, injector=injector)
