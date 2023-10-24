#!/usr/bin/env python3
""" create a function that returns a tuple """


def index_range(page: int, page_size: int) -> tuple:
    """ create a tuple containing page and the page_size """
    # index start at 0
    # take the first page and remvove -1 and multiple by page size
    # to get the initial index
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
