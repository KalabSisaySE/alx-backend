#!/usr/bin/env python3
"""the `0-simple_helper_function` module
defines the function `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of start index and end index
    based on the given pagination parameter `page`, `page_index`"""
    return ((page - 1) * page_size, page * page_size)
