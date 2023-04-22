import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import math
import unittest
from Probability import *
from Probability import factorial
from descriptive_statistics import *


class TestProbability(unittest.TestCase):
    def test_validate_parameters(self):
        # Test valid input parameters
        self.assertIsNone(validate_parameters(5, 0.5))
        self.assertIsNone(validate_parameters(10, 0.1))
        self.assertIsNone(validate_parameters(100, 0.9))
        # Test invalid n
        with self.assertRaises(ValueError):
            validate_parameters(-1, 0.5)
        with self.assertRaises(ValueError):
            validate_parameters(2.5, 0.5)
        # Test invalid p
        with self.assertRaises(ValueError):
            validate_parameters(10, -0.1)
        with self.assertRaises(ValueError):
            validate_parameters(10, 1.1)

    def test_factorial(self):
        # Test valid input parameters
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        # Test invalid input
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(ValueError):
            factorial(-5)
        with self.assertRaises(TypeError):
            factorial(2.5)

    def test_binomial_coefficient(self):
        # Test valid input parameters
        self.assertEqual(binomial_coefficient(5, 0), 1)
        self.assertEqual(binomial_coefficient(5, 1), 5)
        self.assertEqual(binomial_coefficient(5, 2), 10)
        self.assertEqual(binomial_coefficient(10, 5), 252)
        # Test invalid input
        with self.assertRaises(ValueError):
            binomial_coefficient(5, -1)
        with self.assertRaises(ValueError):
            binomial_coefficient(2.5, 2)

    def test_pmf(self):
        # Test valid input parameters
        self.assertAlmostEqual(pmf(0, 5, 0.5), 0.03125)
        self.assertAlmostEqual(pmf(1, 5, 0.5), 0.15625)
        self.assertAlmostEqual(pmf(2, 5, 0.5), 0.3125)
        self.assertAlmostEqual(pmf(3, 5, 0.5), 0.3125)
        self.assertAlmostEqual(pmf(4, 5, 0.5), 0.15625)
        self.assertAlmostEqual(pmf(5, 5, 0.5), 0.03125)
        # Test invalid input
        with self.assertRaises(ValueError):
            pmf(-1, 5, 0.5)
        with self.assertRaises(ValueError):
            pmf(6, 5, 0.5)

    def test_cdf(self):
        # Test valid input parameters
        self.assertAlmostEqual(cdf(0, 5, 0.5), 0.03125)
        self.assertAlmostEqual(cdf(1, 5, 0.5), 0.1875)
        self.assertAlmostEqual(cdf(2, 5, 0.5), 0.5)
        self.assertAlmostEqual(cdf(3, 5, 0.5), 0.8125)
        self.assertAlmostEqual(cdf(4, 5, 0.5), 0.96875)
        self.assertAlmostEqual(cdf(5, 5, 0.5), 1.0)
        # Test invalid input
        with self.assertRaises(ValueError):
            cdf(-1, 5, 0.5)
        with self.assertRaises(ValueError):
            cdf(6, 5, 0.5)


# -----------------------------------------------------------------------------------------------------------------------


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)


if __name__ == "__main__":
    main()
