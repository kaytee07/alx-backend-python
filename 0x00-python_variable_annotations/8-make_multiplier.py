#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float
multiplier as argument and returns a function that multiplies a
float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies the float by a multiplier
    Parameters:
          multiplier(float): The multiplier value
    Returns:
          Callable[[float], float]: The multiplier function'
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
