#!/usr/bin/env python3
"""
type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum list of float and int and return float
    """
    sum: float = 0

    for x in mxd_lst:
        sum += x
    return sum
