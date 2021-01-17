#!/usr/bin/python3
""" find a peak funct"""


def find_peak(list_of_integers):
    """ sorted peak"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
