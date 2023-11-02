from typing import List
from infra.external_api.base.base_api import BaseAPI, MethodType
from infra.external_api.weatherforecast.model.weatherforecast import WeatherForecast


class WeatherForecastAPI(BaseAPI):
    def __init__(self):
        super().__init__("https://api.open-meteo.com/v1")
        self._lock = object()

    async def get_actual_temperature_by_location(self, latitude, longitude) -> WeatherForecast:
        time_zone="America/Sao_Paulo"

        url = f"/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&timezone={time_zone}"

        type = await self.call_api(MethodType.GET, url, WeatherForecast)

        return type