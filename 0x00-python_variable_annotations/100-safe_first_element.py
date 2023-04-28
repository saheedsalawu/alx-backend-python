#!/usr/bin/env python3
"""Augmentation of the following code with the correct duck-typed annotations"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """types the elements of the input are not know"""
    if lst:
    
        return lst[0]
    
    else:
        return None
