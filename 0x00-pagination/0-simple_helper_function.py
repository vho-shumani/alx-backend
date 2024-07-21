#!/usr/bin/env python3
"""Module return range of indexes for a pagination"""


def index_range(page, page_size):
    """Determine and return the range of indexes to return in a
    list for those particular pagination parameters

    Arge:
        page(int): the page number.
        page_size: the size per page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
