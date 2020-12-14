from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Literal




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


class EmployeeScheme(BaseModel):
    name: str
    email: EmailStr
    age: int
    company: str
    join_date: datetime
    job_title: str
    gender: Literal["male", "female", "other"]
    salary: int

    # class Config:
    #     fields = {'name': Scheme.name,
    #               'email': Scheme.email,
    #               'age': Scheme.age,
    #               'company': Scheme.company,
    #               'join_date': Scheme.join_date,
    #               'job': Scheme.job_title,
    #               'gender': Scheme.gender,
    #               'salary': Scheme.salary}
