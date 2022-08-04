#!/usr/bin/env python3
"""
Defines sum_mixed_list
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    returns the sum of things in the list
    """
    total: float = 0
    for i in mxd_list:
        total += i
    return total
