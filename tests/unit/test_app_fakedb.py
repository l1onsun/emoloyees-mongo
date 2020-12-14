import pytest
from httpx import AsyncClient
from app.main import app, get_database, ApiEmployee
from database.scheme import Constants
from datetime import datetime

# strange test, but for example

class FakeDB:
    def __getitem__(self, item):
        assert item == Constants.employee
        return FakeCollection()


class FakeCollection:
    def find(self, query):
        return FakeCursor(query)


class FakeCursor:
    def __init__(self, query):
        self.query = query

    async def to_list(self, unnecessary):
        return [ApiEmployee(name="fake", company="fake", email="fake@email.fake",
                            age=99, join_date=datetime(2020, 1, 1), job_title="fake",
                            gender="other", salary=1234
                            ) for i in range(len(self.query))]


def fake_get_database():
    return FakeDB()


app.dependency_overrides[get_database] = fake_get_database


@pytest.fixture(scope="function")
async def client():
    async with AsyncClient(app=app, base_url="http://testserver") as client:
        yield client

@pytest.mark.parametrize(
    "url,query_len",
    [("/employee", 0),
     ("/employee?name=John Titor", 1),
     ("/employee?company=Abra&company=Cadabra", 1),
     ("/employee?company=Apple&job=director&name=Steve Jobs", 3)]
)
@pytest.mark.asyncio
async def test_app(client, url, query_len):
    result = await client.get(url)
    assert len(result.json()) == query_len
