#!/usr/bin/python3
"""Documentation for a number_of_lines function"""


def number_of_lines(filename=""):
    """Returns the number of lines in the current file
    Args:
        filename (str): the filename to open
    Returns:
        the number of lines in the file
    """

    lines = 0
    with open(filename, encoding='utf-8') as f:
        for i in f:
            lines += 1
        return lines
