from .prod_config import ProdConfig
from .dev_config import DevConfig

configurations = {
    "production": ProdConfig,
    "development": DevConfig,
    "default": DevConfig,
}
