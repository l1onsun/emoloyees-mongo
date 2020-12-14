from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import  Literal

# same as EmployeeScheme, but potentially could be different
class ApiEmployee(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: Literal["male", "female", "other"]
    salary: int
