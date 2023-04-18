import unittest
from parameter_estimation import *


class TestParameterEstimation(unittest.TestCase):

    def setUp(self):
        self.sample_data = [8, 6, 7, 9, 5, 8, 7, 6, 10, 6]

    def test_estimate_parameters(self):
        n_estimate, p_estimate = estimate_parameters(self.sample_data)
        self.assertEqual(n_estimate, 10)
        self.assertAlmostEqual(p_estimate, 0.7, places=1)

    def test_estimate_parameters_empty_data(self):
        with self.assertRaises(ValueError):
            estimate_parameters([])

    def test_log_likelihood(self):
        p_estimate = 0.7
        log_likelihood_value = log_likelihood(p_estimate, self.sample_data)
        self.assertAlmostEqual(log_likelihood_value, -18.3302, places=4)

    def test_mle_estimate_parameters(self):
        n_estimate, p_estimate = mle_estimate_parameters(self.sample_data)
        self.assertEqual(n_estimate, 10)
        self.assertAlmostEqual(p_estimate, 0.7, places=1)

    def test_mle_estimate_parameters_empty_data(self):
        with self.assertRaises(ValueError):
            mle_estimate_parameters([])

    def test_confidence_interval_normal_approximation(self):
        lower_bound, upper_bound = confidence_interval_normal_approximation(self.sample_data, confidence_level=0.95)
        self.assertAlmostEqual(lower_bound, 0.4160, places=4)
        self.assertAlmostEqual(upper_bound, 0.9840, places=4)

    def test_confidence_interval_normal_approximation_empty_data(self):
        with self.assertRaises(ValueError):
            confidence_interval_normal_approximation([])

    def test_confidence_interval_clopper_pearson(self):
        lower_bound, upper_bound = confidence_interval_clopper_pearson(self.sample_data, confidence_level=0.95)
        self.assertAlmostEqual(lower_bound, 0.6213, places=4)
        self.assertAlmostEqual(upper_bound, 0.8052, places=4)

    def test_confidence_interval_clopper_pearson_empty_data(self):
        with self.assertRaises(ValueError):
            confidence_interval_clopper_pearson([])

    def test_confidence_interval_agresti_coull(self):
        lower_bound, upper_bound = confidence_interval_agresti_coull(self.sample_data, confidence_level=0.95)
        self.assertAlmostEqual(lower_bound, 1, places=4)
        self.assertAlmostEqual(upper_bound, 1, places=4)

    def test_confidence_interval_agresti_coull_empty_data(self):
        with self.assertRaises(ValueError):
            confidence_interval_agresti_coull([])

    def test_confidence_interval_agresti_coull_invalid_confidence_level(self):
        with self.assertRaises(ValueError):
            confidence_interval_agresti_coull(self.sample_data, confidence_level=-0.5)


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)


if __name__ == "__main__":
    main()

