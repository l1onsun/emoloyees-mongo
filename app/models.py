from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import  Literal
from database.scheme import SchemeConfig

# same as EmployeeScheme, but potentially could be different
class ApiEmployee(BaseModel):
    name: str = Field(..., alias=SchemeConfig.employee_name)
    email: EmailStr = Field(..., alias=SchemeConfig.employee_email)
    age: int = Field(..., alias=SchemeConfig.employee_age)
    company: str = Field(..., alias=SchemeConfig.employee_company)
    join_date: datetime = Field(..., alias=SchemeConfig.employee_join_date)
    job_title: str = Field(..., alias=SchemeConfig.employee_job_title)
    gender: Literal["male", "female", "other"] = Field(..., alias=SchemeConfig.employee_gender)
    salary: int = Field(..., alias=SchemeConfig.employee_salary)
