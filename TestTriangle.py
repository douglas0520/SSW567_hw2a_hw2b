import unittest
from classify_triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class ClassifyingTriangle(unittest.TestCase):
    """ClassifyingTriangles : list of test cases for various inputs in the
    classify triangle program"""

    def test_right_triangle_a(self):
        """test_right_triangle_a : test case for a right triangle
        returns : Triangle_Is_Right, "3,4,5 is a Right triangle"""
        self.assertEqual(
            classify_triangle(3, 4, 5), "Triangle_Is_Right", "3,4,5 is a Right triangle"
        )

    def test_right_triangle_b(self):
        """test_right_triangle_b : test case for a right triangle
        returns : Triangle_Is_Right, "5,3,4 is a Right triangle"""

        self.assertEqual(
            classify_triangle(5, 3, 4), "Triangle_Is_Right", "5,3,4 is a Right triangle"
        )

    def test_equilateral_triangles(self):
        """test_equilateral_triangles :test case for equilateral triangles
        returns: Triangle_Is_Equilateral, 1,1,1 should be equilateral"""
        self.assertEqual(
            classify_triangle(1, 1, 1),
            "Triangle_Is_Equilateral",
            "1,1,1 should be equilateral",
        )

    def test_isosceles(self):
        """test_isosceles : test case for isosceles triangles
        returns: Triangle_Is_Isosceles, 3,3,4 is an isosceles triangle"""
        self.assertEqual(
            classify_triangle(3, 3, 4),
            "Triangle_Is_Isosceles",
            "3,3,4 is an isosceles triangle",
        )

    def test_scalene(self):
        """test_scalene : test case for scalene triangles
        returns : Triangle_Is_Scalene, 5,7,9 is an scalene triangle"""
        self.assertEqual(
            classify_triangle(5, 7, 9),
            "Triangle_Is_Scalene",
            "5,7,9 is an scalene triangle",
        )

    def test_input_limit_max(self):
        """test_input_limit_max : test if the input is beyond the preset max amount
        returns : Input_limit  "Invalid_Input_Reached_Limit",
            "Input_Limit_Reached (> 200)","""
        self.assertEqual(
            classify_triangle(300, 78, 360),
            "Invalid_Input_Reached_Limit",
            "Input_Limit_Reached (> 200)",
        )

    def test_input_limit_min(self):
        """test_input_limit_min : test if the input is beyond the preset min amount
        returns : Input_limit  "Invalid_Input_Reached_Limit",
            "Input_Limit_Reached (< 0)","""
        self.assertEqual(
            classify_triangle(-10, 10, 10),
            "Invalid_Input_Reached_Limit",
            "Input_Limit_Reached (< 0)",
        )

    def test_is_a_triangle(self):
        """test_is_a_triangle : tests if the inputs correlate to an actual triangle
        returns: "Invalid_Input_Not_A_Triangle",
            "1,10,23 is not a triangle" """
        self.assertEqual(
            classify_triangle(1, 10, 23),
            "Invalid_Input_Not_A_Triangle",
            "1,10,23 is not a triangle",
        )

    def test_float_numbers(self):
        """test_float_number : tests is the input used is a float, the program only takes in integer inputs
        returns : "Invalid_Input_Using_Float",
            "Input = Float" """
        self.assertEqual(
            classify_triangle(1.1, 2.2, 3.3),
            "Invalid_Input_Using_Float",
            "Input = Float",
        )


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
