#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int=10)-> float:
    time_delay = random.uniform(0,max_delay)
    await asyncio.sleep(time_delay)
    return time_delay

print(asyncio.run(wait_random(5)))