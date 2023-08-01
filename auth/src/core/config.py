import os
from logging import config as logging_config

from pydantic import BaseSettings

from core.logger import LOGGING


class Settings(BaseSettings):
    # Применяем настройки логирования
    logging_config.dictConfig(LOGGING)

    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = 'movies_auth'

    # Настройки Redis
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379

    # Настройки Elasticsearch
    ELASTIC_HOST: str = '127.0.0.1'
    ELASTIC_PORT: int = 9200

    # Корень проекта
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        env_file = '.env'


settings = Settings()
