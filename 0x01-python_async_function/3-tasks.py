#!/usr/bin/env python3
"""
function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an
integer max_delay and returns a asyncio.Task.
"""
import asyncio


wait_random = __import__('0-basic_async_suntax').wait_random


def task_wait_random(max_delay=10):
    """
    takes an integer max delay and returns aysnc.io Task

    Args:
        max_delay (float): Maximum delay in seconds (default is 10)

    Returns:
        asyncio.Task: Task object for the wait_random coroutine.
    """
    if max_delay < 0:
        raise ValueError("max_delay cannot be negative")

    return asyncio.create_task(wait_random(max_delay))
