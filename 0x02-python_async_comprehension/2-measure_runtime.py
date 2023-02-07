#!/usr/bin/env python3
"""measure_runtime of coroutine"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime coroutine"""
    start: float = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end: float = time()
    result: float = end - start
    return result