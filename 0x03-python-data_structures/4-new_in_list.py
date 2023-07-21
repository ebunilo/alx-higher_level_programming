#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replace an element in a list without modifying the original list

    Args:
        my_list (any type): list to be modified
        idx (_type_): index position of element to be modified
        element (_type_): element to be modified

    Returns:
        new list
        original list if idx is negative
        original list if idx is out of range
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    new_list = my_list[:]
    new_list[idx] = element

    return new_list
