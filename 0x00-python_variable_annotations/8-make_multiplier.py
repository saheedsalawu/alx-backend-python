#!/usr/bin/env python3
"""the function make_multiplier that takes a float multiplier"""
import typing
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiplier_func(number: float) -> float:
        return multiplier * number
    return multiplier_func
