#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    n = 0
    e = 0

    for t in my_list:
        n += t[0] * t[1]
        e += t[1]

    return (n / e)
