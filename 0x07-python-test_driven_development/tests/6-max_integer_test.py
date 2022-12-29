"""Module for testing the max_integer function from the my_module module
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class for testing the max_integer function
    """

    def test_max_integer(self):
        """
        Test the max_integer function with different lists of integers
        """
        # Test lists with positive integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 2]), 3)
        self.assertEqual(max_integer([1]), 1)

        # Test lists with negative integers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -2, -3, -2]), -1)
        self.assertEqual(max_integer([-1]), -1)

        # Test empty list
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
