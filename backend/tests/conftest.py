from typing import AsyncGenerator

import pytest_asyncio
from httpx import AsyncClient
from main import app


@pytest_asyncio.fixture()
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
