#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replace an element of a list at a specific position

    Args:
        my_list (any type): list of elements
        idx (int): index of element to be replaced
        element (any type): element to replace with
    """
    if idx < 0:
        return my_list
    if idx > len(my_list) - 1:
        return my_list

    my_list[idx] = element

    return my_list
