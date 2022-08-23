#!/usr/bin/env python3
"""
Defines a function wait_random
"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes in an integer and generates a random value
    between 0 and max-delay and delays for that amount of
    time then returns the ransom number
    """
    to_wait = random.uniform(0, max_delay)  # time to delay
    await asyncio.sleep(to_wait)
    return to_wait
