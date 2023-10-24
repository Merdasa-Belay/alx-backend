#!/usr/bin/env python3
""" implemented a Server class to work with data """


import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int) -> tuple:
        """ create a tuple containing page and the page_size """
        # index start at 0
        # take the first page and remvove -1 and multiple by page size
        # to get the initial index
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ get items in a page """
        assert type(page) == int
        assert page > 0
        assert type(page_size) == int
        assert page_size > 0

        start, end = self.index_range(page, page_size)

        csv_file = self.dataset()

        list_result = []

        if start >= len(self.dataset()):
            return list_result

        return csv_file[start:end]
