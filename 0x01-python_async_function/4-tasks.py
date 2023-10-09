#!/usr/bin/env python3
"""
async routine called wait_n that takes in 2 int arguments (in this
order): n and max_delay. You will spawn wait_random n times with
the specified max_delay
"""
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return task wait_random n times

    Args:
        n (int): number of times to return wait_random

    Return:
         wait_random (list): list of wait random n times
    """
    list_of_rand = []
    for i in range(n):
        list_of_rand.append(await task_wait_random(max_delay))
    return sorted(list_of_rand)
