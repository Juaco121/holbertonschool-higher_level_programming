#!/usr/bin/python3
"""Documentation for simple add integer function"""


def add_integer(a, b=98):
    """Adds two integers together
    Args:
        a (int): first value to add
        b (int, optional): second value to add
    Returns:
        the sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
