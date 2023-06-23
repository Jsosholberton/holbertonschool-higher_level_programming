#!/usr/bin/python3
"""Definition of the function"""


def pascal_triangle(n):
    """
    Description:
    ------------
        list of row for print a pascal triangle
    Args:
    -----
        n (int): size of the triangle
    Return:
    -------
        The list of rows for be printed
        """

    triangle = []
    if n <= 0:
        return triangle

    for index in range(n):
        row = [1]
        if triangle:
            pr_row = triangle[-1]
            new_row = [pr_row[j] + pr_row[j+1] for j in range(len(pr_row) - 1)]
            row.extend(new_row)
            row.append(1)
        triangle.append(row)

    return triangle
