#!/usr/bin/env python3
"""async function with annotation"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay : int) -> asyncio.Task:
    """task that waits for a random number of seconds
       between 0 and max_delay"""
    task = asyncio.create_task(wait_random(max_delay))
    return task