#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cp_dic = a_dictionary.copy()
    for ke, va in cp_dic.items():
        if va == value:
            del a_dictionary[ke]
    return a_dictionary
