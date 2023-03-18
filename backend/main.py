import asyncio
import time

from fastapi import FastAPI
from schemas import TestResponse

app = FastAPI(title="Task for WhyNot")
lock = asyncio.Lock()


def monotonic() -> float:
    return time.time()


async def work() -> None:
    await asyncio.sleep(3)


@app.get("/test", response_model=TestResponse)
async def handler() -> TestResponse:
    ts1 = monotonic()

    # Одновременно в этом with может находится только одна корутина
    async with lock:
        await work()

    ts2 = monotonic()
    return TestResponse(elapsed=ts2 - ts1)
