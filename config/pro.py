from .base import Config


class ProConfig(Config):
    DEBUG = False
    DB_URI = "postgresql://admin:passwd@blog-container-postgres:8082"


config = ProConfig()