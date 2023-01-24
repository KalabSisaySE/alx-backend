#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """instantiates a new `Server` object"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """returns the cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """paginate based on `index`, `page_size` and
        the current state of the dataset (deletion reslilience)"""
        idx_ds = self.indexed_dataset()
        if type(index) is int:
            assert index < len(idx_ds)
        items = []
        i = index
        while (len(items) < page_size) and i <= int(list(idx_ds)[-1]):
            if idx_ds.get(i):
                items.append(idx_ds.get(i))
            i = i + 1

        if idx_ds.get(i):
            next_idx = i
        else:
            while not idx_ds.get(i):
                i = i + 1

        return {
            'index': index,
            'next_index': next_idx,
            'page_size': len(items),
            'data': items
        }
