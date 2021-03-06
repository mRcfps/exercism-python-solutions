"""
Notes regarding the implementation of smallest_palindrome and
largest_palindrome:

Both functions must take two keyword arguments:
    max_factor -- int
    min_factor -- int, default 0

Their return value must be a tuple (value, factors) where value is the
palindrome itself, and factors is an iterable containing both factors of the
palindrome in arbitrary order.
"""

import unittest

from palindrome_products import smallest_palindrome, largest_palindrome


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class PalindromesTests(unittest.TestCase):
    def test_smallest_palindrome_from_single_digit_factors(self):
        value, factors = smallest_palindrome(min_factor=1, max_factor=9)
        self.assertEqual(value, 1)
        self.assertFactorsEqual(factors, {(1, 1)})

    def test_largest_palindrome_from_single_digit_factors(self):
        value, factors = largest_palindrome(min_factor=1, max_factor=9)
        self.assertEqual(value, 9)
        self.assertFactorsEqual(factors, {(1, 9), (3, 3)})

    def test_smallest_palindrome_from_double_digit_factors(self):
        value, factors = smallest_palindrome(min_factor=10, max_factor=99)
        self.assertEqual(value, 121)
        self.assertFactorsEqual(factors, {(11, 11)})

    def test_largest_palindrome_from_double_digit_factors(self):
        value, factors = largest_palindrome(min_factor=10, max_factor=99)
        self.assertEqual(value, 9009)
        self.assertFactorsEqual(factors, {(91, 99)})

    def test_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = smallest_palindrome(min_factor=100, max_factor=999)
        self.assertEqual(value, 10201)
        self.assertFactorsEqual(factors, {(101, 101)})

    def test_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest_palindrome(min_factor=100, max_factor=999)
        self.assertEqual(value, 906609)
        self.assertFactorsEqual(factors, {(913, 993)})

    @unittest.skip('computation-intensive')
    def test_smallest_palindrome_from_four_digit_factors(self):
        value, factors = smallest_palindrome(min_factor=1000, max_factor=9999)
        self.assertEqual(value, 1002001)
        self.assertFactorsEqual(factors, {(1001, 1001)})

    @unittest.skip('computation-intensive')
    def test_largest_palindrome_from_four_digit_factors(self):
        value, factors = largest_palindrome(min_factor=1000, max_factor=9999)
        self.assertEqual(value, 99000099)
        self.assertFactorsEqual(factors, {(9901, 9999)})

    def test_empty_for_smallest_palindrome_if_none_in_range(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = smallest_palindrome(min_factor=1002,
                                                 max_factor=1003)

    def test_empty_for_largest_palindrome_if_none_in_range(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = largest_palindrome(min_factor=15, max_factor=15)

    def test_error_for_smallest_if_min_is_more_than_max(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = smallest_palindrome(min_factor=10000,
                                                 max_factor=1)

    def test_error_for_largest_if_min_is_more_than_max(self):
        with self.assertRaisesWithMessage(ValueError):
            value, factors = largest_palindrome(min_factor=2, max_factor=1)

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

    def assertFactorsEqual(self, actual, expected):
        self.assertEqual(set(map(frozenset, actual)),
                         set(map(frozenset, expected)))


if __name__ == '__main__':
    unittest.main()
