from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '..', '.env'), extra='ignore')

    OPENAI_API_KEY: str = "CHAVE_NAO_ENCONTRADA"

# Instância única para ser importada por outros módulos
settings = Settings()