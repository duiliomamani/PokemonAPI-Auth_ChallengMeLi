from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CurrentWeatherForecast:
    time: Optional[str]
    interval: Optional[float]
    temperature: Optional[float]
    def to_class(payload):
        return CurrentWeatherForecast(
            payload.get("time", None),
            payload.get("interval", None),
            payload.get("temperature_2m", None),
        )

@dataclass
class WeatherForecast:
    latitude: Optional[float]
    longitude: Optional[float]
    current: Optional[CurrentWeatherForecast]

    def to_class(payload):
        from infra.external_api.weatherforecast.model.weatherforecast import CurrentWeatherForecast

        return WeatherForecast(
            payload.get("latitude", None),
            payload.get("longitude", None),
            CurrentWeatherForecast.to_class(payload.get("current", None))
        )
