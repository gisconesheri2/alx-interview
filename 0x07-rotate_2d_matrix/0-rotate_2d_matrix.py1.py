#!/usr/bin/python3
"""Rotate a matrix through 90 degrees"""


def rotate_2d_matrix(matrix):
    """Rotate a matrix through 90 degrees"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):

            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for r in range(len(matrix)):
        matrix[r].reverse()
