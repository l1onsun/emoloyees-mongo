from functools import lru_cache

from pydantic import BaseSettings, Field


@lru_cache
def get_env():
    return EnvSettings()


class EnvSettings(BaseSettings):
    allow_drop_tables: bool = Field(False, env='ALLOW_DROP_TABLES')

    mongo_db: str = Field(..., env='POSTGRES_DB')
    mongo_user: str = Field(..., env='POSTGRES_USER')
    mongo_password: str = Field(..., env='POSTGRES_PASSWORD')
    mongo_host: str = Field(..., env='POSTGRES_HOST')
    mongo_port: str = Field(..., env='POSTGRES_PORT')

    # postgres_dsn: PostgresDsn = None
    # postgres_asyncpg_dsn: PostgresAsyncDsn = None


class TestP(BaseSettings):
    x: int
    y: int
    z: int

    def __post_init__(self):
        self.z = self.x + self.y
