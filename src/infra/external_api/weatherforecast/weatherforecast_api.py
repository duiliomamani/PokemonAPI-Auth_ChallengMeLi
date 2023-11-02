from extensions.logger import get_logger
from infra.external_api.base.base_api import BaseAPI, MethodType
from infra.external_api.weatherforecast.model.weatherforecast import WeatherForecast

logger = get_logger(__name__)

class WeatherForecastAPI(BaseAPI):
    def __init__(self):
        super().__init__("https://api.open-meteo.com/v1")
        self._lock = object()

    # Method to get current temperature by location
    async def get_actual_temperature_by_location(self, latitude, longitude) -> WeatherForecast:
        try:
            url = f"/forecast"
            
            # Parameters for the API call
            parameters={"latitude" : latitude, "longitude": longitude, "current": "temperature_2m", "time_zone": "America/Sao_Paulo"}

            type = await self.call_api(type_method=MethodType.GET, resource=url, response_type=WeatherForecast, parameters=parameters)

            return type
        except Exception as e:
            logger.error(f"Error {__name__}")
            raise e
        finally:
            logger.info(f"End {__name__}")