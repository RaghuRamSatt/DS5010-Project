import unittest
import numpy as np
from simulation import BinomialSimulation


class TestBinomialSimulation(unittest.TestCase):

    def test_simulation_run(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertIsNotNone(results)

    def test_simulation_results_length(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertEqual(len(results), 1000)

    def test_invalid_n_trials(self):
        with self.assertRaises(ValueError):
            sim = BinomialSimulation(-1, 0.5, 1000)

    def test_invalid_p_success(self):
        with self.assertRaises(ValueError):
            sim = BinomialSimulation(10, -0.5, 1000)

    def test_invalid_n_experiments(self):
        with self.assertRaises(ValueError):
            BinomialSimulation(10, 0.5, -1)

    def test_histogram_plot_before_simulation(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        with self.assertRaises(ValueError):
            sim.plot_histogram()

    def test_success_probability_evolution_before_simulation(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        with self.assertRaises(ValueError):
            sim.plot_success_probability_evolution()

    def test_invalid_test_type(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        with self.assertRaises(ValueError):
            sim.perform_hypothesis_testing("invalid_test_type")

    def test_hypothesis_testing_before_simulation(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        with self.assertRaises(ValueError):
            sim.perform_hypothesis_testing("proportion_z_test", successes1=5, trials1=10, successes2=5, trials2=10)

    def test_cross_validate_hypothesis_testing_before_simulation(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        with self.assertRaises(ValueError):
            sim.cross_validate_hypothesis_testing("proportion_z_test", successes1=5, trials1=10, successes2=5, trials2=10)

    def test_invalid_n_folds(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        with self.assertRaises(ValueError):
            sim.cross_validate_hypothesis_testing("proportion_z_test", n_folds=1, successes1=5, trials1=10, successes2=5, trials2=10)

    def test_missing_required_arguments_proportion_z_test(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        with self.assertRaises(ValueError):
            sim.perform_hypothesis_testing("proportion_z_test")

    def test_missing_required_arguments_fishers_exact_test(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        with self.assertRaises(ValueError):
            sim.perform_hypothesis_testing("fishers_exact_test")

    def test_missing_required_arguments_chi_square_test(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        with self.assertRaises(ValueError):
            sim.perform_hypothesis_testing("chi_square_test")

    def test_zero_trials(self):
        sim = BinomialSimulation(0, 0.5, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertTrue(np.all(results == 0))

    def test_zero_experiments(self):
        sim = BinomialSimulation(10, 0.5, 0)
        sim.run_simulation()
        results = sim.get_results()
        self.assertEqual(len(results), 0)

    def test_p_success_zero(self):
        sim = BinomialSimulation(10, 0, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertTrue(np.all(results == 0))

    def test_p_success_one(self):
        sim = BinomialSimulation(10, 1, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertTrue(np.all(results == 10))

    def test_large_n_trials(self):
        sim = BinomialSimulation(10**6, 0.5, 100)
        sim.run_simulation()
        results = sim.get_results()
        self.assertEqual(len(results), 100)

    def test_large_n_experiments(self):
        sim = BinomialSimulation(10, 0.5, 10**6)
        sim.run_simulation()
        results = sim.get_results()
        self.assertEqual(len(results), 10**6)

    def test_large_p_success(self):
        with self.assertRaises(ValueError):
            BinomialSimulation(10, 2, 1000)

    def test_small_p_success(self):
        with self.assertRaises(ValueError):
            BinomialSimulation(10, -0.1, 1000)

    def test_minimum_valid_values(self):
        sim = BinomialSimulation(1, 0, 1)
        sim.run_simulation()
        results = sim.get_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], 0)

    def test_maximum_valid_values(self):
        sim = BinomialSimulation(1, 1, 1)
        sim.run_simulation()
        results = sim.get_results()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0], 1)

    def test_results_are_integers(self):
        sim = BinomialSimulation(10, 0.5, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertTrue(np.all(np.equal(np.mod(results, 1), 0)))

    def test_results_within_valid_range(self):
        n_trials = 10
        sim = BinomialSimulation(n_trials, 0.5, 1000)
        sim.run_simulation()
        results = sim.get_results()
        self.assertTrue(np.all(results >= 0))
        self.assertTrue(np.all(results <= n_trials))

def main():
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=3)


if __name__ == "__main__":
    main()


