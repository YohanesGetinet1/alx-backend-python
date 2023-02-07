#!/usr/bin/env python3
"""async_comprehension"""

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension()-> list[float]:
    """async_comprehension coroutine"""
    return [x async for x in async_generator()]
