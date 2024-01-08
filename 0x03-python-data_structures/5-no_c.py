#!/usr/bin/python3
def no_c(my_string):
    n_string = my_string.translate({ord(x): None for x in 'cC'})
    return n_string
