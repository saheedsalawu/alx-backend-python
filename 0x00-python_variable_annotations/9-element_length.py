#!/usr/bin/env python3
"""this function’s as a parameters and return values with the appropriate types"""

import typing
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """return i and lst"""
    return [(i, len(i)) for i in lst]
