import os

basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    """Base config vars."""
    # Change the secret key in production run.
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    POKE_API= os.environ.get("POKE_API", os.path.join(basedir, ".poke_api.endpoint"))
    WEATHER_API= os.environ.get("WEATHER_API", os.path.join(basedir, ".weather_api.endpoint"))
    DEBUG = False
