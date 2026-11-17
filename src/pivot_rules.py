"""Pivoting rules for the simplex method (tableau form).

Each function takes a simplex tableau in basic form, where row 0 holds the
reduced costs and column 0 holds the right-hand side, and returns the
(row, column) index of the pivot entry.
"""

import numpy as np


def find_pivot_largest_subscript(tableau):
    """
    Using the largest subscript rule (opposite of Bland's rule) and the
    minimum ratio test, find the pivot entry in the tableau.

    Parameters
    ----------
    tableau : array
        The simplex method tableau in basic form

    Returns
    -------
    final_r, final_s : integer
        Row and column indexes of the pivot

    Notes
    -----
    Assumes that there is a negative reduced cost that we can pivot on.
    """
    M, N = tableau.shape
    m = M-1
    n = N-1

    # Largest subscript rule: find the last negative reduced cost
    final_s = n
    while final_s >= 1 and tableau[0, final_s] >= 0:
        final_s -= 1

    # Minimum ratio test plus largest subscript rule
    final_r = 0
    theta_star = np.inf
    for i in range(1, m+1):
        if tableau[i, final_s] > 0:
            if tableau[i, 0] / tableau[i, final_s] < theta_star:
                final_r = i
                theta_star = tableau[i, 0] / tableau[i, final_s]

    return final_r, final_s


def find_pivot_largest_coefficient(tableau):
    """
    Using the largest coefficient rule and the minimum ratio test,
    find the pivot entry in the tableau.

    Parameters
    ----------
    tableau : array
        The simplex method tableau in basic form

    Returns
    -------
    final_r, final_s : integer
        Row and column indexes of the pivot

    Notes
    -----
    Assumes that there is a negative reduced cost that we can pivot on.
    """
    M, N = tableau.shape
    m = M-1
    n = N-1

    # Largest coefficient rule: find the MOST negative reduced cost
    final_s = -1
    most_negative = 0
    for s in range(1, n+1):
        if tableau[0, s] < most_negative:
            most_negative = tableau[0, s]
            final_s = s

    # Minimum ratio test plus largest coefficient rule
    final_r = 0
    theta_star = np.inf
    for i in range(1, m+1):
        if tableau[i, final_s] > 0:
            if tableau[i, 0] / tableau[i, final_s] < theta_star:
                final_r = i
                theta_star = tableau[i, 0] / tableau[i, final_s]

    return final_r, final_s
