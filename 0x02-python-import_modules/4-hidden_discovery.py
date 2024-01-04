#!/usr/bin/python3

if __name__ == "__main__":
    
    """ Display the names associated with the hidden_4 module."""

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
