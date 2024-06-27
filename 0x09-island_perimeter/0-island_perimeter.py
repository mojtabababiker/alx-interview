#!/usr/bin/python3
"""Solve the island perimeter problem
"""


def island_perimeter(grid: list):
    """Calculate the perimeter of the island inside the grid if
    available

    parameters:
    -----------
    grid: list of list of integers, that represent the water (0)
    and island (1)

    returns:
    -----------
    perimeter: int, the perimeter of the island if found

    description:
    ------------
    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn't have “lakes” (water inside that isn't connected
    to the water surrounding the island).
    """
    perimeter = 0

    if not isinstance(grid, list):
        return 0

    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if grid[row][col] == 1:
                if grid[row][col - 1] == 0:
                    perimeter += 1

                if grid[row][col + 1] == 0:
                    perimeter += 1

                if grid[row - 1][col] == 0:
                    perimeter += 1

                if grid[row + 1][col] == 0:
                    perimeter += 1

    return perimeter
