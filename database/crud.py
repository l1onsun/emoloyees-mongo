from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List
from database.scheme import Scheme


async def find_employee(db: AsyncIOMotorDatabase,
                        name: List[str] = None, job: List[str] = None, company: List[str] = None):
    employee = db[Scheme.employee]
    query = {}
    if name:
        query[Scheme.name] = {"$in": name}
    if job:
        query[Scheme.job_title] = {"$in": job}
    if company:
        query[Scheme.company] = {"$in": company}
    cursor = employee.find(query)
    return await cursor.to_list(None)
