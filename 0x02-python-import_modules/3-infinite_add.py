#!/usr/bin/python3
if __name__ == "__main__":

    "Display the sum of all provided arguments."
    import sys

    sume = 0
    for i in range(len(sys.argv) - 1):
        sume += int(sys.argv[i + 1])
    print("{}".format(sume))
