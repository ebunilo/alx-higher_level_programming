#!/usr/bin/python3


def no_c(my_string):
    """Remove all characters c and C from a string

    Args:
        my_string: the string to remove character from

    Returns:
        string
    """
    new_string = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            new_string += letter

    return new_string
