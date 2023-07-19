#!/usr/bin/python3
"""Print the ASCII alphabets in lowercase, not followed by a newline"""
for i in range(97, 123):
    print("{}".format(chr(i)), end="")
