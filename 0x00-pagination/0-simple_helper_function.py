#!/usr/bin/env python3
""" THis scirpt shall return a tuple of size two start & end"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ this instnce shall return tuple with range start and size"""
    fin_size = page * page_size
    commence_size = fin_size - page_size

    return (commence_size, fin_size)
