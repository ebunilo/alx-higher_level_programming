#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments"""
    import sys

    args = sys.argv
    count = len(sys.argv) - 1
    if count == 0:
        print("{} arguments.".format(count))
    elif count == 1:
        print("{} argument:".format(1))
        print("{}: {}".format(1, args[1]))
    else:
        print("{} arguments:".format(count))
        for i in range(count):
            print("{}: {}".format(i + 1, args[i + 1]))
