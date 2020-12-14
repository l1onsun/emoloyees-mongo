import pytest
import asyncio

from motor.motor_asyncio import AsyncIOMotorDatabase
from database.main import get_database
from database.manage import import_employee_json, drop_employee, create_employee_index
from database.crud import find_employee
from database.scheme import Constants


# redefine event_loop to `module` scope
# because we don't want to drop the database before each test
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="module")
async def seeded_database() -> AsyncIOMotorDatabase:
    await drop_employee()
    await import_employee_json()
    await create_employee_index()
    return get_database()


@pytest.mark.asyncio
async def test_get_all(seeded_database: AsyncIOMotorDatabase):
    employee_list = await find_employee(seeded_database)
    assert len(employee_list) == 600
    fields = {Constants.name, Constants.company, Constants.job_title, Constants.salary, Constants.gender,
              Constants.join_date, Constants.age, Constants.email}
    for emp in employee_list:
        assert len(emp.keys()) == len(fields) + 1  # +1 is ObjectID
        for field in fields:
            assert field in emp.keys()


@pytest.mark.parametrize(
    "test_companies,expected_result_len",
    [(["Google", "LinkedIn"], 191),
     (["Twitter"], 75)]
)
@pytest.mark.asyncio
async def test_query_company(seeded_database: AsyncIOMotorDatabase, test_companies, expected_result_len):
    employee_list = await find_employee(seeded_database, companies=test_companies)
    assert len(employee_list) == expected_result_len
    for emp in employee_list:
        assert emp['company'] in test_companies


@pytest.mark.parametrize(
    "test_jobs,expected_result_len",
    [(["developer", "designer"], 214),
     (["director"], 77)]
)
@pytest.mark.asyncio
async def test_query_jobs(seeded_database: AsyncIOMotorDatabase, test_jobs, expected_result_len):
    employee_list = await find_employee(seeded_database, jobs=test_jobs)
    assert len(employee_list) == expected_result_len
    for emp in employee_list:
        assert emp['job_title'] in test_jobs

# todo: test name
