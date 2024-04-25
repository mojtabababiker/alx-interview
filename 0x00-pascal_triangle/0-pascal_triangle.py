#!/usr/bin/python3
"""
Technical interview problems:
    Pascal triangle
"""


def pascal_triangle(n):
    """
    pascal_traingle(n): create pascal triangle with n levels

    Parameters:
    -----------
    n: int, integer that represents the number of levels
    return:
    -----------
    pascal_array: list, list of lists that represents the pascal traingle
    """
    pascal_array = []

    for lvl in range(n):
        prev_arr = pascal_array[lvl - 1] if lvl > 0 else None
        current_arr = []
        for i in range(0, lvl):
            value = prev_arr[i - 1] + prev_arr[i] if i != 0 else 1
            current_arr.append(value)
        current_arr.append(1)
        pascal_array.append(current_arr)

    return pascal_array
