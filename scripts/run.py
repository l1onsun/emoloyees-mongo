import fire
import subprocess
from typing import Literal
import asyncio
import dotenv
import os

from database.manage import create_employee_index, import_employee_json, drop_employee

ENVS = {
    "dev": "dotenv/.env.dev",
    "prod": "dotenv/.env.prod",
    "docker": "dotenv/.env.docker",
}


class MainRunner():
    def __init__(self, mode: Literal["dev", "prod", "docker"]):
        assert mode in ENVS.keys()
        dotenv.load_dotenv(ENVS[mode])
        self._mode = mode

    def start(self):
        if self._mode == "dev":
            subprocess.run(["uvicorn", "app.main:app", "--reload", "--port", os.getenv("GUNICORN_PORT")])
        elif self._mode in {"prod", "docker"}:
            subprocess.run(["gunicorn", "app.main:app",
                            "-k", "uvicorn.workers.UvicornWorker", "-c", "config/gunicorn_conf.py"])
        return self

    def build(self):
        assert self._mode == "docker"
        subprocess.run(["docker-compose", "build"])
        return self

    def up(self):
        assert self._mode == "docker"
        subprocess.run(["docker-compose", "up"])
        return self

    def database(self):
        return DatabaseRunner()

    def pytest(self, test_running: bool = False):
        cmd = ["python", "-m", "pytest"]
        if not test_running:
            cmd.append("--ignore=tests/integration")
        subprocess.run(cmd)

    def __call__(self):
        pass


class DatabaseRunner():
    def __init__(self):
        self._loop = asyncio.new_event_loop()

    def drop(self):
        self._loop.run_until_complete(drop_employee())
        return self

    def seed(self):
        self._loop.run_until_complete(import_employee_json())
        return self

    def create_index(self):
        self._loop.run_until_complete(create_employee_index())
        return self

    def __call__(self):
        self._loop.close()
        pass


if __name__ == '__main__':
    fire.Fire(MainRunner)
