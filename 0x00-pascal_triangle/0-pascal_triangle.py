#!/usr/bin/python3
"""Implement a pascal triangle
"""


def pascal_triangle(n):
    """Implement a pascal triangle
        n(int): number of row of the triangle
        Return: list of lists with inner lists representing
        the rows
    """
    triangle = []

    if n <= 0:
        return triangle

    new_row = []
    prev_row = []

    for row in range(n):
        new_row.append(1)
        for idx in range(len(prev_row)):
            try:
                new_num = prev_row[idx] + prev_row[idx + 1]
                new_row.append(new_num)
            except IndexError:
                new_row.append(1)

        triangle.append(new_row)
        prev_row = new_row
        new_row = []

    return triangle
