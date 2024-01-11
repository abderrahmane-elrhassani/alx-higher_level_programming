#!/usr/bin/python3
def complex_delete(a_dictionary, v):
    list_keys = list(a_dictionary.keys())

    for vc in list_keys:
        if v == a_dictionary.get(vc):
            del a_dictionary[vc]

    return (a_dictionary)
