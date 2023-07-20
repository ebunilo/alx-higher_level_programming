#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print all integers in a list

    Args:
        my_list (list, optional): the list of integers to print. Defaults to [].

    Returns:
        None

    """
    for number in my_list:
        print("{:d}".format(number))
