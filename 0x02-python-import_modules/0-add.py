#!/usr/bin/python3
"""
Import the function def add(a, b) from the file 
and print the result of the addition 1 + 2 = 3
"""
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
