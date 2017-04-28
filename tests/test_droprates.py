import unittest
from fractions import Fraction
from code import droprates


class TestDroprates(unittest.TestCase):
    def test_at_least_x_successes(self):
        self.assertEqual(droprates.at_least(0, 3, Fraction(1, 3)), 27 / 27)
        self.assertEqual(droprates.at_least(1, 3, Fraction(1, 3)), 19 / 27)
        self.assertEqual(droprates.at_least(2, 3, Fraction(1, 3)), 7 / 27)
        self.assertEqual(droprates.at_least(3, 3, Fraction(1, 3)), 1 / 27)

    def test_exactly_x_successes(self):
        self.assertEqual(droprates.exact(0, 3, Fraction(1, 3)), 8 / 27)
        self.assertEqual(droprates.exact(1, 3, Fraction(1, 3)), 12 / 27)
        self.assertEqual(droprates.exact(2, 3, Fraction(1, 3)), 6 / 27)
        self.assertEqual(droprates.exact(3, 3, Fraction(1, 3)), 1 / 27)
        print(droprates.at_least(1, 10, Fraction(1, 10)))


if __name__ == '__main__':
    unittest.main()
