#!/usr/bin/python3
"""
Rotating n x n matrix inplace
"""


def rotate_2d_matrix(matrix):
    """
    Rotate 2d matrix 90 degrees clockwise in-place

    Parameters:
    ------------
    matrix: list[list]
          list of lists that need to be rotated
    """
    for index, row in enumerate(matrix):
        for col in range(index, len(row)):
            temp = matrix[index][col]
            matrix[index][col] = matrix[col][index]
            matrix[col][index] = temp
        matrix[index].reverse()
