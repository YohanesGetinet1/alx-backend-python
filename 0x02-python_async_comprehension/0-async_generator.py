#!/usr/bin/env python3
"""
coroutine async_generator
Write coroutine async_generator that takes two arguments
loops 10x, wait 1sec each time asynchronously
yield random number between 0-10 using random module
"""
import asyncio
import random
from typing import Generator
 
async def async_generator() -> Generator [float, None, None]:
    """async_generator"""
    for x in range(0, 10,1):
        await asyncio.sleep(1)
        yield random.uniform(0,10)