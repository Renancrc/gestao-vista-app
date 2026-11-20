"""Configuração lida de variáveis de ambiente (ou do arquivo .env).

Nada de senha ou segredo escrito no código: tudo vem do ambiente.
Localmente, o docker compose lê o .env; na nuvem, os valores virão do
AWS Secrets Manager (Fase 3).
"""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "Gestão à Vista Microsoft"
    environment: str = "local"

    # postgresql+psycopg://usuario:senha@host:porta/banco
    database_url: str = "postgresql+psycopg://gestao:gestao@localhost:5432/gestao"
    # redis://host:porta/numero-do-banco
    redis_url: str = "redis://localhost:6379/0"

    # Origens que o navegador pode usar para chamar a API (CORS)
    cors_origins: list[str] = ["http://localhost:3000", "http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
