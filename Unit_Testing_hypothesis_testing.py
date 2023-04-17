import unittest
import numpy as np
from hypothesis_testing import *


class TestHypothesisTesting(unittest.TestCase):
    def test_proportion_z_test(self):
        # Test with 0 successes in both groups
        self.assertRaises(ValueError, proportion_z_test, 0, 0, 0, 0)

        # Test with 0 trials in group 1
        self.assertRaises(ValueError, proportion_z_test, 0, 0, 5, 10)

        # Test with 0 trials in group 2
        self.assertRaises(ValueError, proportion_z_test, 5, 10, 0, 0)

        # Test with invalid alternative hypothesis
        self.assertRaises(ValueError, proportion_z_test, 5, 10, 3, 10, alternative='invalid')

        # Test with valid input
        p_value = proportion_z_test(50, 100, 40, 100)
        self.assertAlmostEqual(p_value, 0.155218489684684, places=6)

        # Test with alternative hypothesis 'greater'
        p_value = proportion_z_test(50, 100, 40, 100, alternative='greater')
        self.assertAlmostEqual(p_value, 0.077609244842342, places=6)

        # Test with alternative hypothesis 'less'
        p_value = proportion_z_test(50, 100, 40, 100, alternative='less')
        self.assertAlmostEqual(p_value, 0.922390755157658, places=6)

        # Test with invalid alternative hypothesis
        with self.assertRaises(ValueError):
            proportion_z_test(50, 100, 40, 100, alternative='invalid')

        # Test with zero trials in one of the groups
        with self.assertRaises(ValueError):
            proportion_z_test(50, 100, 0, 0)

    def test_power_analysis_binomial_proportions(self):
        sample_size = power_analysis_binomial_proportions(0.5, 0.4, 0.05, 0.8)
        self.assertEqual(sample_size, 389)

        sample_size = power_analysis_binomial_proportions(0.5, 0.4, 0.05, 0.8, alternative='greater')
        self.assertEqual(sample_size, 307)

        sample_size = power_analysis_binomial_proportions(0.5, 0.4, 0.05, 0.8, alternative='less')
        self.assertEqual(sample_size, 307)

        with self.assertRaises(ValueError):
            power_analysis_binomial_proportions(0.5, 0.4, 0.05, 0.8, alternative='invalid')

    def test_fishers_exact_test(self):
        p_value = fishers_exact_test(50, 100, 40, 100)
        self.assertAlmostEqual(p_value, 0.2007076, places=6)

        p_value = fishers_exact_test(50, 100, 40, 100, alternative='greater')
        self.assertAlmostEqual(p_value, 0.1003538, places=6)

        p_value = fishers_exact_test(50, 100, 40, 100, alternative='less')
        self.assertAlmostEqual(p_value, 0.941142, places=6)

        with self.assertRaises(ValueError):
            fishers_exact_test(50, 100, 40, 100, alternative='invalid')

        with self.assertRaises(ValueError):
            fishers_exact_test(50, -100, 40, 100, alternative='greater')

    def test_chi_square_test(self):
        binomial_data = [(10, 100), (20, 100), (30, 100), (40, 100)]
        p_value = chi_square_test(binomial_data)
        self.assertAlmostEqual(p_value, 0.00016974243555278878, places=6)

        with self.assertRaises(ValueError):
            chi_square_test(binomial_data, expected_proportions=[0.2, 0.3, 0.4])

    def test_g_test_goodness_of_fit(self):
        binomial_data = [(10, 100), (20, 100), (30, 100), (40, 100)]
        p_value = g_test_goodness_of_fit(binomial_data)
        self.assertAlmostEqual(p_value, 9.172704041071622e-05, places=6)

        with self.assertRaises(ValueError):
            g_test_goodness_of_fit(binomial_data, expected_proportions=[0.2, 0.3, 0.4])

    def test_proportion_z_test_zero_trials(self):
        with self.assertRaises(ValueError):
            proportion_z_test(0, 0, 0, 0)

    def test_proportion_z_test_large_numbers(self):
        p_value = proportion_z_test(1000000, 10000000, 2000000, 10000000)
        self.assertAlmostEqual(p_value, 0.0, places=6)

    def test_power_analysis_binomial_proportions_large_numbers(self):
        sample_size = power_analysis_binomial_proportions(0.1, 0.05, 0.01, 0.99)
        self.assertEqual(sample_size, 1334)

    def test_power_analysis_binomial_proportions_small_numbers(self):
        sample_size = power_analysis_binomial_proportions(0.001, 0.0005, 0.05, 0.8)
        self.assertEqual(sample_size, 47058)

    def test_fishers_exact_test_large_numbers(self):
        p_value = fishers_exact_test(1000000, 10000000, 2000000, 10000000)
        self.assertAlmostEqual(p_value, 0.0, places=6)

    def test_fishers_exact_test_zero_trials(self):
        p_value = fishers_exact_test(0, 0, 0, 0)
        self.assertTrue(np.all(np.isnan(p_value)))

    def test_chi_square_test_large_numbers(self):
        binomial_data = [(1000000, 10000000), (2000000, 10000000), (3000000, 10000000), (4000000, 10000000)]
        p_value = chi_square_test(binomial_data)
        self.assertAlmostEqual(p_value, 0.0, places=6)

    def test_chi_square_test_zero_trials(self):
        binomial_data = [(0, 0), (0, 0), (0, 0), (0, 0)]
        p_value = chi_square_test(binomial_data)  # Assuming chi_square_test returns a single value (p_value)
        self.assertTrue(np.isnan(p_value))

    def test_g_test_goodness_of_fit_large_numbers(self):
        binomial_data = [(1000000, 10000000), (2000000, 10000000), (3000000, 10000000), (4000000, 10000000)]
        p_value = g_test_goodness_of_fit(binomial_data)
        self.assertAlmostEqual(p_value, 0.0, places=6)

    def test_g_test_goodness_of_fit_zero_trials(self):
        binomial_data = [(0, 0), (0, 0), (0, 0), (0, 0)]
        p_value = g_test_goodness_of_fit(binomial_data)
        self.assertTrue(np.isnan(p_value))

    def test_proportion_confidence_interval(self):
        # Test with small sample size
        success = 5
        trials = 10
        ci = proportion_confidence_interval(success, trials)
        assert np.allclose(ci, (0.19010248384771922, 0.8098975161522808))

        # Test with large sample size
        success = 500
        trials = 1000
        ci = proportion_confidence_interval(success, trials)
        assert np.allclose(ci, (0.4690102483847719, 0.5309897516152281))

        # Test with invalid input
        success = 'string'
        trials = 10
        with self.assertRaises(ValueError):
            proportion_confidence_interval(success, trials)

        success = 5
        trials = 10
        alpha = 1.1
        with self.assertRaises(ValueError):
            proportion_confidence_interval(success, trials, alpha=alpha)


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)


if __name__ == "__main__":
    main()
