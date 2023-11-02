from dataclasses import dataclass
from typing import List


@dataclass
class WeatherForecast_Types:
    name: str
    temperature_max: int
    temperature_min: int

# Mock Weather Forecast by Type Pokemon
weatherforecast_types_list: List[WeatherForecast_Types] = [
    WeatherForecast_Types(name="fire", temperature_max=None, temperature_min=30),
    WeatherForecast_Types(name="ground", temperature_max=30, temperature_min=20),
    WeatherForecast_Types(name="normal", temperature_max=20, temperature_min=10),
    WeatherForecast_Types(name="water", temperature_max=10, temperature_min=0),
    WeatherForecast_Types(name="ice", temperature_max=0, temperature_min=None),
]

# Method to obtain type with temperature
def get_weather_type(temperature):
    for weather_type in weatherforecast_types_list:
        if (
            weather_type.temperature_min is None
            or temperature >= weather_type.temperature_min
        ) and (
            weather_type.temperature_max is None
            or temperature < weather_type.temperature_max
        ):
            return weather_type.name
