from pydantic_settings import BaseSettings


# Class to hold the database connection settings, which are loaded from environment variables defined in a .env file
class Settings(BaseSettings):
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGHOST: str
    PGPORT: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create an instance of the Settings class to load the configuration values from the .env file
settings = Settings()
