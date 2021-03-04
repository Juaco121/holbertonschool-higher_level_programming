#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    aux_list = []
    aux_list2 = []
    res_up = 0
    res_dow = 0
    for m in my_list:
        n = m[0] * m[1]
        d = m[1]
        aux_list.append(n)
        aux_list2.append(d)
    for up_n in aux_list:
        res_up += up_n
    for dow_n in aux_list2:
        res_dow += dow_n
    return res_up / res_dow
