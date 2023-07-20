#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Print all the names defined by compiled module
        Print one name per line in alpha order
        Print only manes that do not start with __
    """
    names = dir(hidden_4)
    names.sort()
    for name in names:
        if name[:2] != "__":
            print("{}".format(name))

