import unittest
from sources import circle


class TestCircumference(unittest.TestCase):  # defining a series of tests
    """
    Test the circumference function from the circle module.
    """

    def test_unit_circle(self):  # defining the first test in this series
        """
        Test that the circumference function calculates the
        circumference of a unit circle correctly.
        """
        ans = circle.circumference(1)   # calculate the answer given by the
        # user-defined function
        self.assertEqual(ans, 6.283)    # compare with the correct answer

    def test_circumference_dp(self):  # defining the second test in this series
        """
        Test that the dp variable works for the circumference
        function.
        """
        ans = circle.circumference(2.7, 10)     # calculate the answer given
        #  by the user-defined function
        self.assertEqual(ans, 16.9646003294)    # compare with the correct
        # answer
