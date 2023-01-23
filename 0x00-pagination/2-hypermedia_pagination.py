#!/usr/bin/env python3
"""the 2-hypermedia_pagination module
defines the function `index_range` and the class `Server`
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of start index and end index
    based on the given pagination parameter `page`, `page_index`"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        data_set = self.dataset()
        for num in [page, page_size]:
            assert isinstance(num, int) and num > 0
        indexes = index_range(page=page, page_size=page_size)
        len_ds = len(data_set)
        if len_ds >= indexes[1]:
            return [data_set[index] for index in range(indexes[0], indexes[1])]
        elif len_ds >= indexes[0] and len_ds < indexes[1]:
            return [data_set[index] for index in range(indexes[0], len_ds)]

        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """returns a dict of page info based on `page` and `page_size`"""
        data_set = self.dataset()
        current_dataset = self.get_page(page=page, page_size=page_size)

        return {
            "page_size": len(current_dataset),
            "page": page,
            "data": current_dataset,
            "next_page": (page + 1) if (current_dataset != []) else None,
            "prev_size": (page - 1) if (page - 1 > 0) else None,
            "total_pages": math.ceil(len(data_set) / page_size),
        }
