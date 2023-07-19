#!/usr/bin/python3
"""
Print all possible combinations of two digits
    Numbers must be separated by , followed by a space
    The two digits must be different
    01 and 10 are considered the same combination of 0 and 1
    Print only the smallest combination of two digits
    The last number should be followed by a new line
"""
for i in range(0, 10):
    for j in range(i+1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
