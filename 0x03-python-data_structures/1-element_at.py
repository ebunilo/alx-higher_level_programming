#!/usr/bin/python3


def element_at(my_list, idx):
    """Retrieve an element from a list

    Args:
        my_list (any): list of elements
        idx (int): index of element to retrieve

    Returns:
        element at index idx
        None if idx is negative
        None if idx is out of range
    """
    if idx < 0:
        return None
    if idx > len(my_list) - 1:
        return None

    return (my_list[idx])
