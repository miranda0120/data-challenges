# pylint: disable=missing-docstring

import random
def sudoku_solver(grid):
    """Sudoku solver"""
    row = set()
    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
