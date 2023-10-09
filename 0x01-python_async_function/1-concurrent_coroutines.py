#!/usr/bin/env python3
"""
async routine called wait_n that takes in 2 int arguments (in this
order): n and max_delay. You will spawn wait_random n times with
the specified max_delay
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return wait_random n times

    Args:
        n (int): number of times to return wait_random

    Return:
         wait_random (list): list of wait random n times
    """
    list_of_rand = []
    for i in range(n):
        list_of_rand.append(await wait_random(max_delay))
    return list_of_rand
