#!/usr/bin/env python3
"""
Defines to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    Returns a tuple of k and square of v
    """
    return (k, v**2)