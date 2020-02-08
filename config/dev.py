from .base import Config


# loading settings
class DevConfig(Config):
    DEBUG = True
    DB_URI = "postgresql://admin:passwd@blog-container-postgres:8082"


config = DevConfig()