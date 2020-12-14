from functools import lru_cache

from pydantic import BaseSettings, Field
from typing import Optional

@lru_cache
def get_env():
    return EnvSettings()


class EnvSettings(BaseSettings):
    allow_drop_tables: bool = Field(False, env='ALLOW_DROP_TABLES')

    mongo_db: str
    mongo_user: str
    mongo_auth_db: Optional[str] = None
    mongo_password: str
    mongo_host: str
    mongo_port: int
    mongo_min_connections: int
    mongo_max_connections: int

    # mongo_seed_collection: str
    mongo_seed_json: str
    # postgres_dsn: PostgresDsn = None
    # postgres_asyncpg_dsn: PostgresAsyncDsn = None

