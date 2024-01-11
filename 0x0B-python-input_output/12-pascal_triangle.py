#!/usr/bin/python3
"""a Pascal's Triangle function."""


def pascal_triangle(n):
    """creates a Pascal's triangle of size n.

    Returns a list representing a Pascal's triangle.
    """
    if n <= 0:
        return []

    tris = [[1]]
    while len(tris) != n:
        tri = tris[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        tris.append(temp)
    return tris
