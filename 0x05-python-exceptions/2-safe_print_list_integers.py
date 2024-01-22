#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    This function prints the first x integers from a list using the format s     pecifier "{:d}". It employs a try/except block to handle exceptions. Th     e list, my_list, may contain various types (e.g., integer, string), but     only integers are printed. Integers are displayed on the same line, fol     lowed by a new line. Any non-integer values in the list are silently sk     ipped. The function returns the actual number of integers successfully      printed.

   Args:
    x: Number of elements to access in my_list.

   Returns:
    The real number of integers printed.
   """
    count = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[item], end='')
                count += 1
            except IndexError:
                break
    print()
    return count
