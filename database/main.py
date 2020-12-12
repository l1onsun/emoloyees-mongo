from config.environ import get_env
from pymongo import MongoClient


def get_database():
    env = get_env()
    client = MongoClient(env.mongo_host, env.mongo_port)
    db = client[env.mongo_db]
    return db