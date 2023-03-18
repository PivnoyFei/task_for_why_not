import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def get_response(ac: AsyncClient) -> float:
    response = await ac.get("/test")
    assert response.status_code == 200
    return response.json()["elapsed"]


async def test_get(ac: AsyncClient) -> None:
    check_time = [await get_response(ac) for _ in range(3)]
    for i in check_time:
        assert i >= 3
