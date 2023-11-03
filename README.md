# Challenge MeLi - PokeWeather API

## Descripción
Este proyecto representa un desafío realizado para MercadoLibre en el área de Security IAM. La **PokeWeather API** combina la diversión de Pokémon con datos meteorológicos, proporcionando una interfaz para obtener información sobre Pokémon específicos y sus hábitats climáticos asociados.

## Pasos para Dockerizar el Proyecto
1. Construir la imagen Docker:
    ```bash
    docker build -t challenge-meli-poke-api -f build/Dockerfile .
    ```

2. Levantar el contenedor Docker:
    ```bash
    docker run -d -p 5000:5000 -e POKE_API=$("https://pokeapi.co/api/v2/") -e WEATHER_API=$("https://api.open-meteo.com/v1/") -e FLASK_ENV=$("development") -e FLASK_RUN_PORT=$("5000") challenge-meli-poke-api
    ```

## Librerías Utilizadas
- **Flask**: Un framework web ligero para construir aplicaciones web en Python.
- **Flask-Restx**: Una extensión de Flask que facilita la creación de APIs RESTful con documentación automática.
- **Flask-Injector**: Una librería de inyección de dependencias para Flask.

## Documentación de Swagger
La documentación de Swagger se encuentra en el path `/api/docs`.

## Método de Autenticación (AuthN)
La PokeWeather API utiliza un método de autenticación basado en ApiKey. Se ha implementado un autorizador que valida la ApiKey proporcionada, otorgando acceso a los recursos de la API y determinando sobre qué método se está intentando ejecutar. En caso de que la ApiKey no sea válida, se lanzará una excepción de 401 (No autorizado), y si el usuario intenta acceder a recursos prohibidos, se generará una excepción de 403 (Acceso prohibido).

## Configuración Local
Para levantar el proyecto de manera local, crea los siguientes archivos:
- **.poke_api.endpoint**: Contiene la URL del servicio Poke API (Ejemplo: https://pokeapi.co/api/v2/).
- **.weather_api.endpoint**: Contiene la URL del servicio Weather API (Ejemplo: https://api.open-meteo.com/v1/).

Asigna estas variables de entorno en el momento de levantar el contenedor Docker:
- **POKE_API**: Asigna la URL del servicio Poke API.
- **WEATHER_API**: Asigna la URL del servicio Weather API.
- **FLASK_ENV**: Configura el ambiente de Flask, con `production` para producción y `development` para desarrollo.
- **FLASK_RUN_PORT**: Especifica el puerto en el que se ejecutará Flask.

## Ejemplos de API Keys
### Cliente MeLi IAM (Con todos los permisos)
api_key="NzNjMmEwY2QtMGE1YS00NTJhLTk5MTEtNjAwNGJlYWQ3Nzlk"

### Cliente Company IAM (Sin permisos)
api_key="OGNmOGIzNWYtNjZhNS00NjE4LTk0ZWItODk3MDc5ZDY3ZmZl"


---

_Challenge MeLi IAM_
