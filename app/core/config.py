from pydantic import BaseSettings
from dotenv import dotenv_values

config = dotenv_values(".env")

class Settings(BaseSettings):
    APP_HOST: str = "localhost"
    APP_PORT: int = 8000
    DEBUG: bool = True
    LOG_LEVEL: str = "info"
    DATABASE_URL: str = f"postgresql://{config['DB_LOGIN']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_NAME']}"
    # REDIS_URL: str = "redis://localhost:6379/0"
    # VARNISH_HOST: str = "localhost"
    # VARNISH_PORT: int = 80
    # RABBITMQ_URL: str = "amqp://guest:guest@localhost:5672/"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
