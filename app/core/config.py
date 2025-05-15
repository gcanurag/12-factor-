from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "SentimentAnalyzer"
    environment: str = "development"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
