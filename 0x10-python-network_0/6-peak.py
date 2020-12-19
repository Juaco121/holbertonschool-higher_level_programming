#!/usr/bin/python3
"""Function find_peak that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Function that finds a peak in a list of unsorted integers."""

    if not list_of_integers:
        return None

    peak = list_of_integers[0]

    for n in list_of_integers:
        if n > peak:
            peak = n

    return peak
    