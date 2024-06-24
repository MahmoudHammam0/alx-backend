#!/usr/bin/env python3
""" Simple pagination module """
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple containing a start index and an end index """
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
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        indices = index_range(page, page_size)
        data = self.dataset()
        try:
            return data[indices[0]:indices[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """ return a dictionary of metadata for hypermedia pagination """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = self.get_page(page, page_size)
        indices = index_range(page, page_size)
        dataset = self.dataset()
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {"page_size": page_size,
                "page": page,
                "data": data,
                "next_page": next_page,
                "prev_page": prev_page,
                "total_pages": total_pages}
