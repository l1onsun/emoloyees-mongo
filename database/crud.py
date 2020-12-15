from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
from database.scheme import SchemeConfig


async def find_employee(db: AsyncIOMotorDatabase,
                        names: List[str] = None, jobs: List[str] = None, companies: List[str] = None):
    employee = db[SchemeConfig.collection_employee]
    query = {}
    if names:
        query[SchemeConfig.employee_name] = {"$in": names}
    if jobs:
        query[SchemeConfig.employee_job_title] = {"$in": jobs}
    if companies:
        query[SchemeConfig.employee_company] = {"$in": companies}
    cursor = employee.find(query)
    return await cursor.to_list(None)
