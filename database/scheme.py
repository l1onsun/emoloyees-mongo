from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Literal



# constants
class SchemeConfig:
    collection_employee = "employee"
    employee_name = "name"
    employee_email = "email"
    employee_age = "age"
    employee_company = "company"
    employee_join_date = "join_date"
    employee_job_title = "job_title"
    employee_gender = "gender"
    employee_salary = "salary"
    employee_indexes = [(employee_company, 1), (employee_job_title, 1), (employee_name, 1)]


# class to validate data input to mongo
class EmployeeScheme(BaseModel):
    name: str = Field(..., alias=SchemeConfig.employee_name)
    email: EmailStr = Field(..., alias=SchemeConfig.employee_email)
    age: int = Field(..., alias=SchemeConfig.employee_age)
    company: str = Field(..., alias=SchemeConfig.employee_company)
    join_date: datetime = Field(..., alias=SchemeConfig.employee_join_date)
    job_title: str = Field(..., alias=SchemeConfig.employee_job_title)
    gender: Literal["male", "female", "other"] = Field(..., alias=SchemeConfig.employee_gender)
    salary: int = Field(..., alias=SchemeConfig.employee_salary)
