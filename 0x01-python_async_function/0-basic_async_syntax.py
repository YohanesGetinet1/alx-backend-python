#!/usr/bin/env python3
"""an asynchronous coroutine"""
import asyncio
import random

async def wait_random(max_delay: int=10)-> float:
    """wait for a random number of seconds between 0 and max_delay"""
    time_delay = random.uniform(0,max_delay)
    await asyncio.sleep(time_delay)
    return time_delay

# print(asyncio.run(wait_random(5)))