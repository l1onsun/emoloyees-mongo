from config.environ import get_env

from functools import lru_cache
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from devtools import debug


@lru_cache
def get_db_client() -> AsyncIOMotorClient:
    env = get_env()
    connect_uri = "mongodb://{}:{}@{}:{}".format(env.mongo_user, env.mongo_password, env.mongo_host, env.mongo_port)
    if env.mongo_auth_db is not None:
        connect_uri += "/{}".format(env.mongo_auth_db)
    return AsyncIOMotorClient(connect_uri,
                              maxPoolSize=env.mongo_max_connections,
                              minPoolSize=env.mongo_min_connections)


@lru_cache
def get_database() -> AsyncIOMotorDatabase:
    env = get_env()
    return get_db_client()[env.mongo_db]
