#!/usr/bin/python3
"""
Technical interview problems: Minimum operations
The problem is to find the minimum number of operations (copyAll and paste)
needed to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations needed to get the n characters.

    Parameters:
    -------------
    n: int, the required number of character repetition

    return:
    number_of_ops: int, the minimum number of operations
    """
    if not isinstance(n, int) or n <= 1:
        return 0

    number_of_hs = 1
    clipboard = 0
    number_of_ops = 0

    clipboard = number_of_hs  # copy
    number_of_hs += clipboard  # paste
    number_of_ops += 2  # increment number of operations

    while n > number_of_hs: # n = 12, number_of_hs = 2, clipboard = 1, number_of_ops = 2
        if n % (number_of_hs + clipboard) == 0:
            number_of_hs += clipboard
            number_of_ops += 1
        else:
            clipboard = number_of_hs
            number_of_hs += clipboard
            number_of_ops += 2

    return number_of_ops