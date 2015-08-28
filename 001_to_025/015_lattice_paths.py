# coding: utf-8

"""
Lattice paths

Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

# This is a k-combination problem.
# Given 40 steps, you can select 20 of them to be right-steps. Each new combination will generate a new path.

from math import factorial


def get_path_count(grid_height, grid_width):
    return factorial(grid_height + grid_width) / (factorial(grid_height) * factorial(grid_width))


print get_path_count(2, 2)  # test
print get_path_count(20, 20)  # solution
