#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This function prints a specified number (x) of elements from a list. All elements should be printed on the same line, followed by a new line. To achieve this, you must use a try/except block. Importing any module or using the len() function is not allowed.

Args:
my_list: A list of elements.
x: The number of elements to print.

Returns:
The actual number of elements successfully printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
