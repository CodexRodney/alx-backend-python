#!/usr/bin/env python3
"""
Defines a function task_wait_n
"""

from typing import Callable, List
task_wait_random: Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls task_wait_random n times with  specified
    max_delay
    """
    delays = []  # list of delays
    for i in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    sorted_delays = sorted(delays)
    return sorted_delays
