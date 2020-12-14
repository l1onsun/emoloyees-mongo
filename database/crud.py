from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
from database.scheme import Constants


async def find_employee(db: AsyncIOMotorDatabase,
                        name: List[str] = None, job: List[str] = None, company: List[str] = None):
    employee = db[Constants.employee]
    query = {}
    if name:
        query[Constants.name] = {"$in": name}
    if job:
        query[Constants.job_title] = {"$in": job}
    if company:
        query[Constants.company] = {"$in": company}
    cursor = employee.find(query)
    return await cursor.to_list(None)
