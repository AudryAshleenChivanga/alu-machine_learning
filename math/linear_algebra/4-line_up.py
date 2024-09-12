#!/usr/bin/env python3

"""
        The function adds two arrays element-wise.
    """


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
    - arr1 (list of ints/floats): The first array.
    - arr2 (list of ints/floats): The second array.

    Returns:
    - list: A new list containing the element-wise sum of arr1 and arr2.
    - None: If arr1 and arr2 are not of the same shape.
    """
    if len(arr1) != len(arr2):
        return None  # Return None if the arrays are not of the same shape

    # Use list comprehension to add arrays element-wise
    return [a + b for a, b in zip(arr1, arr2)]
