#!/usr/bin/python3
"""
Print the ASCII alphabet in reverse order
alternating lowercase and uppercase (z in lowercase and Y in uppercase)
"""
for i in range(122, 96, -1):
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")
