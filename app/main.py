from fastapi import FastAPI, Depends, Query
from database.main import get_database, get_db_client
from typing import List
from .models import ApiEmployee
from database import crud
from pydantic import constr

app = FastAPI()


@app.on_event("startup")
def init_db():
    # initiate lru_cache
    get_db_client()


@app.on_event("shutdown")
def close_db_client():
    get_db_client().close()

safe_str = constr(regex="^[a-zA-Z0-9 ]+$")

@app.get("/employee", response_model=List[ApiEmployee])
async def get_employee(name: List[safe_str] = Query([]),
                       job: List[safe_str] = Query([]),
                       company: List[safe_str] = Query([]),
                       db=Depends(get_database)):
    return await crud.find_employee(db, name=name, job=job, company=company)
