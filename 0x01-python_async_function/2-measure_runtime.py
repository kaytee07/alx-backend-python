#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as
arguments that measures the total execution time for
wait_n(n, max_delay), and returns total_time / n.
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    time it takes for wait_n to execute divided by n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time() - start
    return elapsed / n
