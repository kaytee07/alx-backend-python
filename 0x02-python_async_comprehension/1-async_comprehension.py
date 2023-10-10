#!/usr/bin/env python3
"""
oroutine called async_comprehension that takes no arguments.
"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 numbers from async_generator and return them

    Args:
        no args

    Returns:
        return a list of random numbers
    """
    return [num async for num in async_generator()]
