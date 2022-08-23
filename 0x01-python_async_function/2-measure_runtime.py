#!/usr/bin/env python3
"""
Defines a function measure time
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n
    then returns totaltime/ n
    """
    starting_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - starting_time
    return total_time / n
