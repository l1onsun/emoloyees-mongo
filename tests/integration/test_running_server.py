import pytest
from httpx import AsyncClient
from config.gunicorn_conf import gunicorn_env


@pytest.fixture(scope="function")
async def client():
    async with AsyncClient(base_url=f"http://localhost:{gunicorn_env.port}") as client:
        yield client


# should be more complex
@pytest.mark.parametrize(
    "url,expected_result_len",
    [("/employee?job=developer&job=designer", 214),
     ("/employee?job=director", 77),
     ("/employee?company=Twitter", 75),
     ("/employee?company=Google&company=LinkedIn", 191)]
)
@pytest.mark.asyncio
async def test_app(client, url, expected_result_len):
    result = await client.get(url)
    assert len(result.json()) == expected_result_len
