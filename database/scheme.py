from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal


# It's not optimal to store constant names this way.
# But i decided, that using ODM like μMongo or writing ODM by self is overkill for small task.

# constants
class Constants:
    employee = "employee"
    name = "name"
    email = "email"
    age = "age"
    company = "company"
    join_date = "join_date"
    job_title = "job_title"
    gender = "gender"
    salary = "salary"
    indexes = [(company, 1), (job_title, 1), (name, 1)]

# validate data, that will be stored in mongo
class EmployeeScheme(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: Literal["male", "female", "other"]
    salary: int