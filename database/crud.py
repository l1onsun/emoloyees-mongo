from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
from database.scheme import Constants


async def find_employee(db: AsyncIOMotorDatabase,
                        names: List[str] = None, jobs: List[str] = None, companies: List[str] = None):
    employee = db[Constants.employee]
    query = {}
    if names:
        query[Constants.name] = {"$in": names}
    if jobs:
        query[Constants.job_title] = {"$in": jobs}
    if companies:
        query[Constants.company] = {"$in": companies}
    cursor = employee.find(query)
    return await cursor.to_list(None)
