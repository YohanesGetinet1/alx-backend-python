#!/usr/bin/env python3
import asyncio
import random

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension()-> list[float]:
    return [x async for x in async_generator()]
# coroutine comprehension  