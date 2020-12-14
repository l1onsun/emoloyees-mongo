from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal


# Didn't found simple way to avoid breaking DRY
# Decided, that using ODMs like μMongo or invent the wheel by self is overkill for small task.
# Anyway, i think, keeping class with constants is better than hardcode

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


# class to validate data input to mongo
class EmployeeScheme(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: Literal["male", "female", "other"]
    salary: int
