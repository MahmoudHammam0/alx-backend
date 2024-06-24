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
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0
        indices = index_range(page, page_size)
        result = []
        with open('Popular_Baby_Names.csv', 'r')  as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i <= indices[0]:
                    continue
                if i > indices[1]:
                    break
                result.append(row)
        return result
