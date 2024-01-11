#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nr = a_dictionary.copy()
    ls = list(nr.keys())

    for a in ls:
        nr[a] *= 2

    return (nr)
