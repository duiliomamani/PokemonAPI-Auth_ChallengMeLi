# Challenge MeLI - PokeWeather API

## Descripción
Este proyecto representa un desafío realizado para MercadoLibre en el área de Security IAM. La **PokeWeather API** combina la diversión de Pokémon con datos meteorológicos, proporcionando una interfaz para obtener información sobre Pokémon específicos y sus hábitats climáticos asociados.

## Pasos para Dockerizar el Proyecto
1. Construir la imagen Docker:
    ```bash
    docker build -t flask-poke-api -f build/Dockerfile .
    ```

2. Levantar el contenedor Docker:
    ```bash
    docker run -d -p 5000:5000 flask-poke-api
    ```

## Librerías Utilizadas
- **Flask**: Un framework web ligero para construir aplicaciones web en Python.
- **Flask-Restx**: Una extensión de Flask que facilita la creación de APIs RESTful con documentación automática.

## Documentación de Swagger
La documentación de Swagger se encuentra en el path `/api/docs`.

## Método de Autenticación (AuthN)
La PokeWeather API utiliza un método de autenticación basado en ApiKey. Se ha implementado un autorizador que valida la ApiKey proporcionada, otorgando acceso a los recursos de la API y determinando sobre qué método se está intentando ejecutar. En caso de que la ApiKey no sea válida, se lanzará una excepción de 401 (No autorizado), y si el usuario intenta acceder a recursos prohibidos, se generará una excepción de 403 (Acceso prohibido).

---

_Para obtener detalles adicionales sobre la implementación de la autenticación y cómo utilizar la API, consulta la documentación incluida en el código fuente o en la interfaz de usuario._
