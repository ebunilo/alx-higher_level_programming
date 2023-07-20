#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list, in reverse order.

    Args:
        my_list (list, optional): list of integers to print. Defaults to [].

    Returns:
        None
    """
    my_list.sort(reverse=True)
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
