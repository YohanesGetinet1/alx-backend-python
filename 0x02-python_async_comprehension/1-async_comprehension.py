#!/usr/bin/env python3
"""async_comprehension"""
from typing import List
result = List[float]

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension()-> result:
    """async_comprehension coroutine"""
    stop = [x async for x in async_generator()]
    return stop
