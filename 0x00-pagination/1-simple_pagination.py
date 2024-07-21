#!/usr/bin/env python3
"""1-simple_pagination.py"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Determine and return the range of indexes to return in a
    list for those particular pagination parameters

    Arge:
        page(int): the page number.
        page_size: the size per page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve the page stipulated by page and page_size"""
        self.dataset()
        page_list = []

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page > 0
        range_index = index_range(page, page_size)
        if range_index[1] > len(self.__dataset):
            return page_list
        for i in range(range_index[0], range_index[1]):
            page_list.append(self.__dataset[i])
        return page_list
