from .base_config import BaseConfig
from .dev_config import DevConfig

configurations = {
    'production': DevConfig,
    'development': DevConfig,
    'default': BaseConfig
}
