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


class TestDescriptiveStatistics(unittest.TestCase):

    def test_mean(self):
        self.assertAlmostEqual(mean(10, 0.5), 5)
        self.assertAlmostEqual(mean(5, 0.2), 1)
        self.assertAlmostEqual(mean(20, 0.8), 16)

    def test_variance(self):
        self.assertAlmostEqual(variance(10, 0.5), 2.5)
        self.assertAlmostEqual(variance(5, 0.2), 0.8)
        self.assertAlmostEqual(variance(20, 0.8), 3.2)

    def test_standard_deviation(self):
        self.assertAlmostEqual(standard_deviation(10, 0.5), 1.5811, places=4)
        self.assertAlmostEqual(standard_deviation(5, 0.2), 0.8944, places=4)
        self.assertAlmostEqual(standard_deviation(20, 0.8), 1.7889, places=4)

    def test_mode(self):
        self.assertEqual(mode(10, 0.5), 5)
        self.assertEqual(mode(5, 0.2), 1)
        self.assertEqual(mode(20, 0.8), 16)

    def test_skewness(self):
        self.assertEqual(skewness(10, 0.5), 0)
        self.assertAlmostEqual(skewness(20, 0.2), 0.33541019662496846)
        self.assertAlmostEqual(skewness(5, 0.2), 0.6708, places=4)
        # calculated_skewness = skewness(5, 0.2)
        # print(f"Calculated skewness: {calculated_skewness}")

    def test_kurtosis(self):
        self.assertAlmostEqual(kurtosis(10, 0.5), -0.2, places=1)
        self.assertAlmostEqual(kurtosis(20, 0.2), 0.0125)

    def test_entropy(self):
        self.assertAlmostEqual(entropy(10, 0.5), 2.706, places=2)
        self.assertAlmostEqual(entropy(20, 0.2), 2.868, places=2)

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
        with self.assertRaises(ValueError):
            validate_parameters(10, 1.5)

# class TestBinomialDistribution(unittest.TestCase):
#
#     def test_mean(self):
#         self.assertEqual(mean(10, 0.5), 5)
#         self.assertEqual(mean(20, 0.2), 4)
#
#     def test_variance(self):
#         self.assertEqual(variance(10, 0.5), 2.5)
#         self.assertEqual(variance(20, 0.2), 3.2)
#
#     def test_standard_deviation(self):
#         self.assertAlmostEqual(standard_deviation(10, 0.5), 1.5811388300841898)
#         self.assertAlmostEqual(standard_deviation(20, 0.2), 1.7888543819998317)
#
#     def test_mode(self):
#         self.assertEqual(mode(10, 0.5), 5)
#         self.assertEqual(mode(20, 0.2), 4)
#
#     def test_skewness(self):
#         self.assertEqual(skewness(10, 0.5), 0)
#         self.assertAlmostEqual(skewness(20, 0.2), 0.33541019662496846)
#
#     def test_kurtosis(self):
#         self.assertAlmostEqual(kurtosis(10, 0.5), -0.2)
#         self.assertAlmostEqual(kurtosis(20, 0.2), 0.0125)
#
#     def test_entropy(self):
#         self.assertAlmostEqual(entropy(10, 0.5), 2.7064289123067764, places=6)
#         self.assertAlmostEqual(entropy(20, 0.2), 2.8685174192809337, places=6)
#
#     def test_validate_parameters(self):
#         self.assertRaises(ValueError, validate_parameters, -1, 0.5)
#         self.assertRaises(ValueError, validate_parameters, 10, -0.5)
#         self.assertRaises(ValueError, validate_parameters, 10, 1.5)
#         self.assertRaises(ValueError, validate_parameters, "10", 0.5)


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)


if __name__ == "__main__":
    main()

