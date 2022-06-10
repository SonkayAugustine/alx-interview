#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    calculate perimeter of the island

    Args:
        grid ([[int]]): is a list of list of integers
    Return: perimeter of the island described in grid
    """
    _sum, limit = (0, 0)
    len_grid, len_col = (len(grid), len(grid[0]))

    for col in range(len_grid):
        _sum += sum(grid[col])
        for row in range(len_col):
            if grid[col][row]:
                if row > 0 and grid[col][row - 1] == 1:
                    limit += 1

                if col > 0 and grid[col - 1][row] == 1:
                    limit += 1
    return _sum * 4 - limit * 2
