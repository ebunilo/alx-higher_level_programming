#!/usr/bin/python3
"""
Import the function def add(a, b) from the file add_0.py 
and print the result of the addition 1 + 2 = 3
"""
from add_0 import add
a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))