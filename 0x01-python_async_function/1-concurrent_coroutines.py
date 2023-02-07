#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay : int = 10) -> list[float]:
    """return the list of all the delays (float values)"""
    delay_list: list=[]
    for i in range(n):
        delay = asyncio.create_task(wait_random(max_delay))
        delay_list.append(delay)
    result_list: list=[]
    for i in asyncio.as_completed(delay_list):
        result: float = await i
        result_list.append(result)
    return result_list 
# print(asyncio.run(wait_n(5, 5)))