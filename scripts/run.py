import fire
import subprocess
from typing import Literal
from config.environ import get_env


class DatabaseRunner():
    def seed(self):
        env = get_env()
        subprocess.run(["mongoimport", "--db", env.mongo_db,
                        "--collection", env.mongo_employee_collection, "--file", env.mongo_seed_json, "--jsonArray"])


class MainRunner():
    def __init__(self, mode: Literal["dev", "prod"]):
        assert mode in {"dev", "prod"}
        self._mode = mode

    def up(self):
        if self._mode == "dev":
            subprocess.run(["uvicorn", "app.main:app", "--reload"])
        elif self._mode == "prod":
            subprocess.run(["gunicorn", "app.main:app",
                            "-k", "uvicorn.workers.UvicornWorker", "-c", "config/gunicorn_conf.py"])

    def db(self):
        return


if __name__ == '__main__':
    fire.Fire(MainRunner)
