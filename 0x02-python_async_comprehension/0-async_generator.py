#!/usr/bin/env python3
'''coroutine async_generator'''
import asyncio
import random
from typing import Generator
 
async def async_generator() -> Generator [float, None, None]:
    '''async_generator'''
    for x in range(0, 10,1):
        await asyncio.sleep(1)
        yield random.randint(0,10)