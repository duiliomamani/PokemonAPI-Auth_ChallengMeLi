import os

from config.base_config import BaseConfig

basedir = os.path.abspath(os.path.dirname(__file__))

class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
