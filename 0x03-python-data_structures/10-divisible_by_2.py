#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mt = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mt.append(True)
        else:
            mt.append(False)
    return mt
