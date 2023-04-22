import sys
import os
current_directory = os.getcwd()
main_directory_path = os.path.abspath(os.path.join(current_directory, '..'))
sys.path.insert(0, main_directory_path)

import unittest
from random_sampling import bernoulli_trial, binomial_sample, generate_binomial_samples


class TestRandomSampling(unittest.TestCase):

    def test_bernoulli_trial(self):
        # Test probability bounds
        with self.assertRaises(ValueError):
            bernoulli_trial(-0.1)
        with self.assertRaises(ValueError):
            bernoulli_trial(1.1)

        # Test expected results
        self.assertIn(bernoulli_trial(0), [0])
        self.assertIn(bernoulli_trial(1), [1])

    def test_binomial_sample(self):
        # Test invalid inputs
        with self.assertRaises(ValueError):
            binomial_sample(-1, 0.5)
        with self.assertRaises(ValueError):
            binomial_sample(10, -0.1)
        with self.assertRaises(ValueError):
            binomial_sample(10, 1.1)

        # Test expected results
        self.assertEqual(binomial_sample(0, 0.5), 0)
        self.assertEqual(binomial_sample(10, 0), 0)
        self.assertEqual(binomial_sample(10, 1), 10)

    def test_generate_binomial_samples(self):
        # Test invalid inputs
        with self.assertRaises(ValueError):
            generate_binomial_samples(0, 10, 0.5)
        with self.assertRaises(ValueError):
            generate_binomial_samples(-1, 10, 0.5)
        with self.assertRaises(ValueError):
            generate_binomial_samples(10, -1, 0.5)
        with self.assertRaises(ValueError):
            generate_binomial_samples(10, 10, -0.1)
        with self.assertRaises(ValueError):
            generate_binomial_samples(10, 10, 1.1)
        with self.assertRaises(ValueError):
            generate_binomial_samples(10, 10, 0.5, seed='invalid')

        # Test sample size and values
        samples = generate_binomial_samples(5, 10, 0.5)
        self.assertEqual(len(samples), 5)
        for sample in samples:
            self.assertTrue(0 <= sample <= 10)

        # Test seed for reproducibility
        samples1 = generate_binomial_samples(5, 10, 0.5, seed=42)
        samples2 = generate_binomial_samples(5, 10, 0.5, seed=42)
        self.assertEqual(samples1, samples2)


def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)


if __name__ == "__main__":
    main()


