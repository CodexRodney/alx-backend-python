#!/usr/bin/env python3
"""
defines function sum_list
"""

from typing import List


def sum_list(x: List[float]) -> float:
    """
    Returns the sum of things in list
    """
    total: float = 0.0
    for i in x:
        total += i
    return total
