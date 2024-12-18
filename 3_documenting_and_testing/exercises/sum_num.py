#!/user/bin/env python3
# -*- coding utf-8 -*-
"""
A module to generate sum

Module contents:
     - Sum_num: Add two numbers and returns the result.

Created on 10 12 24
@author: Muhammad Shahroz
"""

# --- before documenting and testing ---

# def sum_num(a,b)
#     a = 3
#     b = 5
#     return 8

# --- after documenting and testing ---


def sum_num(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If the arguments are not integers.

    Examples:
        >>> sum_num(3, 5)
        8

        >>> sum_num(-1, 1)
        0

        >>> sum_num(0, 0)
        0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    return a + b
