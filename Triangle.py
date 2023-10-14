"""
Module: classify_triangle

This module defines a function for classifying a triangle based on its side lengths.

Author: Douglas Chi
Date: October 14, 2023
"""


def classify_triangle(side_a, side_b, side_c):
    """
    classify_triangle(side_a, side_b, side_c) :  will classify  based on its side inputs.

    side_a : Length of side a.
    side_b : Length of side b.
    side_c : Length of side c.
    Returns: str: The classification of the triangle.

    """

    if side_a > 200 or side_b > 200 or side_c > 200:
        return "Invalid_Input_Reached_Limit"
    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "Invalid_Input_Reached_Limit"
    if not (
        isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)
    ):
        return "Invalid_Input_Using_Float"

    sides = [side_a, side_b, side_c]
    longest_side = max(sides)
    sides.remove(longest_side)
    if longest_side >= sum(sides):
        return "Invalid_Input_Not_A_Triangle"

    if side_a == side_b and side_b == side_a and side_a == side_c:
        return "Triangle_Is_Equilateral"
    elif sides[0] ** 2 + sides[1] ** 2 == (longest_side**2):
        return "Triangle_Is_Right"
    elif (side_a != side_b) and (side_b != side_c) and (side_a != side_b):
        return "Triangle_Is_Scalene"
    return "Triangle_Is_Isosceles"
