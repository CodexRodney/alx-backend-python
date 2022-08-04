#!/usr/bin/env python3
"""
Defines function element_length
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a tuple containing the length
    for each element of lst
    """
    return [(i, len(i)) for i in lst]
