#!/usr/bin/env python3
"""
Defines a function wait_n
"""

from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Calls wait_random n times with  specified
    max_delay
    """
    delays = []  # list of delays
    for i in range(n):
        delay = await wait_random(max_delay)
        delays.append(delay)
    sorted_delays = sorted(delays)
    return sorted_delays
