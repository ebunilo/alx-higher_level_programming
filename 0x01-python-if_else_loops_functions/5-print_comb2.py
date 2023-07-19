#!/usr/bin/python3
"""
Print numbers 0 to 99 separated by , followed by a space
Numbers should be printed in ascending order, with two digits
"""
for number in range(0, 99):
    print("{:02d}, ".format(number), end="")
print("99\n")
