#!/usr/bin/env python3
"""
async_generator that takes no arguments.
"""
import asyncio
import random
for typing import Generator


async def async_generator() -> Generator:
    """
    function loop 10 times each time wait one second before
    returning a random number between 1 and 10

    Args:
        no args

    Return:
        return random floating point numbers betwen 1 - 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
