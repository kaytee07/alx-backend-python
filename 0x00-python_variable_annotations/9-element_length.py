#!/usr/bin/env python3
"""
annotating a functions parameters and return values with the
appropriate types
"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    calculate the length of each element in the input sequence
    """
    return [(i, len(i)) for i in lst]
