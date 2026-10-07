"""Configuración de la API (variables de entorno)."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_prefix="COSMO_API_", extra="ignore")

    # --- Fuente de datos: Apollo (cosmo-web) ---
    # API pública de Apollo (https://apollo.cafe), desplegada desde el repo
    # teamreflex/cosmo-web. Se usa como fuente por defecto.
    apollo_base_url: str = "https://apollo.cafe"

    # --- Fuente de datos: Typesense (opcional, requiere instancia propia) ---
    typesense_url: str | None = None  # p.ej. http://localhost:8108
    typesense_key: str | None = None  # search-only API key (la crea typesense-import)
    typesense_collection: str = "collections"

    # --- Caché simple en memoria ---
    cache_ttl_seconds: int = 300

    app_name: str = "Objekts API"
    app_version: str = "0.1.0"


settings = Settings()
