from pydantic import BaseSettings, Field
from typing import Optional
import multiprocessing

class GunicornEnvSettings(BaseSettings):
    workers_per_core: int = Field(1, env="GUNICORN_WORKERS_PER_CORE")
    max_workers: int = Field(2, env="GUNICORN_MAX_WORKERS")
    web_concurrency: Optional[int] = Field(None, env="GUNICORN_WEB_CONCURRENCY")
    host: str = Field("localhost", env="GUNICORN_HOST")
    port: str = Field("8080", env="GUNICORN_PORT")
    timeout: int = Field(120, env="GUNICORN_TIMEOUT")
    keepalive: int = Field(5, env="GUNICORN_KEEP_ALIVE")

gunicorn_env = GunicornEnvSettings()

def count_workers():
    if gunicorn_env.web_concurrency:
        workers = gunicorn_env.web_concurrency
    else:
        cores = multiprocessing.cpu_count()
        default_web_concurrency = gunicorn_env.workers_per_core * cores
        workers = min(int(default_web_concurrency), gunicorn_env.max_workers)

    assert workers > 0
    return workers


# Gunicorn config
bind = f"{gunicorn_env.host}:{gunicorn_env.port}"
workers = count_workers()
timeout = gunicorn_env.timeout
keepalive = gunicorn_env.keepalive # not a typo
