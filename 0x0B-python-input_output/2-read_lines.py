#!/usr/bin/python3
"""Documentation for a read_lines function"""


def read_lines(filename="", nb_lines=0):
    """Reads and prints a specified number of lines
    Args:
        filename (str): the filename to open
        nb_lines (int): the number of lines to print
    """

    lines = 0
    with open(filename, encoding='utf-8') as f:
        for l in f:
            lines += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= lines:
            print(f.read(), end="")
        else:
            for i in range(nb_lines):
                print(f.readline(), end="")
