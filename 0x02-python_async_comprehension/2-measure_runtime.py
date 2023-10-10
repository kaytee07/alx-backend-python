#!/usr/bin/env python3
"""
measure the total run time to execute async generator
"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure runtime of async comprehension
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.time() - start_time
    return elapsed
