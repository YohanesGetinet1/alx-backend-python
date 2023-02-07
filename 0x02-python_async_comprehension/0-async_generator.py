#!/usr/bin/env python3

import asyncio
import random
 
async def async_generator():
    for x in range(0, 10,1):
        await asyncio.sleep(1)
        yield random.randint(0,10)