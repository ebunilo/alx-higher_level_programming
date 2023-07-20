#!/usr/bin/python3

if __name__ == "__main__":
    """Print the result of additionof all arguments"""
    import sys

    args = sys.argv
    count = len(sys.argv) - 1
    sum_ = 0

    for i in range(count):
        sum_ += int(args[i + 1])
    print("{}".format(sum_))
