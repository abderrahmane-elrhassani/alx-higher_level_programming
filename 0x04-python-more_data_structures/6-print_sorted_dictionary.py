#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ld = list(a_dictionary.keys())
    ld.sort()
    for a in ld:
        print("{}: {}".format(a, a_dictionary.get(a)))
