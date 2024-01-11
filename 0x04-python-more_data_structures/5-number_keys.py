#!/usr/bin/python3
def number_keys(a_dictionary):
    nm = 0
    list_keys = list(a_dictionary.keys())

    for a in list_keys:
        nm += 1

    return (nm)
