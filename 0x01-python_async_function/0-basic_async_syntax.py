#!/usr/bin/env python3
"""
asynchronous coroutine that takes in an integer argument named
wait_random that waits for a random delay between 0 and max_delay 
seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    delay function wait between 0 and max_delay and returns
    a random number between 0 and 10

    args:
         max_delay (float): max delay in seconds

    Returns:
           float: Random delay in seconds

    """
    if max_delay < 0:
        raise ValueError("max_delay cannot be negative")

    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
