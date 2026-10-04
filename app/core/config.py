from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Database connection string will come from the .env file.
    database_url: str

    # Used later when we implement JWT authentication.
    secret_key: str

    # Controls whether the application is running in development mode.
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()