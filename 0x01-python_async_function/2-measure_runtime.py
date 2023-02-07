#!/usr/bin/env python3
"""async function with annotation"""
import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n : int, max_delay : int) -> float:
    """measure runtime of wait_n(n, max_delay)"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    total_time = (start - end)
    return total_time / n

# print(measure_time(5,9))