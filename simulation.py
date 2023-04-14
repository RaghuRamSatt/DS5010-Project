import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hypothesis_testing import proportion_z_test, fishers_exact_test, chi_square_test


class BinomialSimulation:
    """
    A class for simulating binomial experiments.

    Attributes:
        n_trials (int): The number of trials in each experiment.
        p_success (float): The probability of success in each trial.
        n_experiments (int): The number of experiments to simulate.
        results (ndarray or None): An array containing the results of the simulations, or None if the simulation has
        not been run.

    Methods:
       - run_simulation(): Runs the binomial simulation.
       - plot_histogram(bins=None): Plots a histogram of the simulation results.
       - plot_success_probability_evolution(window_size=10): Plots the evolution of success probabilities.
       - perform_hypothesis_testing(test_type, **kwargs): Performs hypothesis testing on the simulated results.
       - cross_validate_hypothesis_testing(test_type, n_folds=5, **kwargs): Performs cross-validation of hypothesis
         testing on the simulated results.
    """

    def __init__(self, n_trials, p_success, n_experiments):
        """Initializes the BinomialSimulation object with the given parameters.

        :param: n_trials (int): The number of trials per experiment.
        :param: p_success (float): The probability of success per trial.
        :param: n_experiments (int): The number of experiments to simulate.
        """
        if n_trials < 0:
            raise ValueError("n_trials must be a non-negative integer.")
        if p_success < 0 or p_success > 1:
            raise ValueError("p_success must be a float between 0 and 1 (inclusive).")
        if n_experiments < 0:
            raise ValueError("n_trials must be a non-negative integer.")

        self.n_trials = n_trials
        self.p_success = p_success
        self.n_experiments = n_experiments
        self.results = None

    def run_simulation(self):
        self.results = np.random.binomial(self.n_trials, self.p_success, size=self.n_experiments)

    def plot_histogram(self, bins=None):
        """Plots a histogram of the results.

        :param: bins (int or sequence of scalars, optional): If bins is an int, it defines the number of equal-width
                bins in the given range (10, by default). If bins is a sequence, it defines the bin edges, including the
                left edge of the first bin and the right edge of the last bin; in this case, bins may be unequally
                spaced

        :return:
                None
        """
        if not self.results:
            raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

        plt.figure()
        sns.histplot(self.results, kde=False, bins=bins, discrete=True)
        plt.axvline(self.n_trials * self.p_success, color='r', linestyle='dashed', linewidth=1)
        plt.title("Histogram of Successes in Binomial Experiments")
        plt.xlabel("Number of Successes")
        plt.ylabel("Frequency")
        plt.show()

    def plot_success_probability_evolution(self, window_size=10):
        """Plots the evolution of success probabilities in the simulated experiments.

        :param: window_size (int, optional): The size of the sliding window to use for calculating the moving average
                (10 by default).

        :return:
                None
    """
        if not self.results:
            raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

        success_probabilities = self.results / self.n_trials
        moving_average = np.convolve(success_probabilities, np.ones(window_size), 'valid') / window_size

        plt.figure()
        plt.plot(moving_average)
        plt.title("Evolution of Success Probabilities in Binomial Experiments")
        plt.xlabel("Experiment Number")
        plt.ylabel("Success Probability")
        plt.show()

    def perform_hypothesis_testing(self, test_type, **kwargs):
        """Performs hypothesis testing on the simulated results using the specified test type and input values provided
            in the kwargs. The input values required depend on the test type being used, and should be provided in the
            kwargs dictionary.

        For example, if test_type is 'proportion_z_test', the kwargs should contain the following keys:
        - successes1: number of successes in the first sample
        - trials1: number of trials in the first sample
        - successes2: number of successes in the second sample
        - trials2: number of trials in the second sample
        - alternative (optional): 'two-sided', 'less', or 'greater'

        :param: test_type (str): The type of hypothesis test to perform ('proportion_z_test', 'fishers_exact_test', or
                'chi_square_test').
        :param: **kwargs: Additional keyword arguments to pass to the hypothesis test function.

        :return:
                float: The p-value resulting from the hypothesis test.
        """

        if self.results is None:
            raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

        if test_type == 'proportion_z_test':
            if 'successes1' not in kwargs or 'trials1' not in kwargs or 'successes2' not in kwargs or 'trials2' not in \
                    kwargs:
                raise ValueError("Missing required arguments for proportion_z_test.")
            p_value = proportion_z_test(kwargs['successes1'], kwargs['trials1'], kwargs['successes2'],
                                        kwargs['trials2'], alternative=kwargs.get('alternative', 'two-sided'))

        elif test_type == 'fishers_exact_test':
            if 'success1' not in kwargs or 'total1' not in kwargs or 'success2' not in kwargs or 'total2' not in kwargs:
                raise ValueError("Missing required arguments for fishers_exact_test.")
            p_value = fishers_exact_test(kwargs['success1'], kwargs['total1'], kwargs['success2'], kwargs['total2'],
                                         alternative=kwargs.get('alternative', 'two-sided'))

        elif test_type == 'chi_square_test':
            if 'binomial_data' not in kwargs:
                raise ValueError("Missing required arguments for chi_square_test.")
            p_value = chi_square_test(kwargs['binomial_data'],
                                      expected_proportions=kwargs.get('expected_proportions', None))

        else:
            raise ValueError("Invalid test_type. Choose from 'proportion_z_test', 'fishers_exact_test', "
                             "or 'chi_square_test'.")

        return p_value

    def calculate_metrics(self, test_data):
        """Calculates various metrics for the binomial experiment

        :param: test_data (list): A list of results for the test data.

        :return:
                dict: A dictionary containing the mean, median, and standard deviation.
        """

        mean = np.mean(test_data)
        median = np.median(test_data)
        std_dev = np.std(test_data)

        return {
            'mean': mean,
            'median': median,
            'std_dev': std_dev
        }

    def cross_validate_hypothesis_testing(self, test_type, n_folds=5, **kwargs):
        """Performs cross-validation of hypothesis testing on the simulated results using the specified test type and
            input values provided in the kwargs. The input values required depend on the test type being used, and should
            be provided in the kwargs dictionary.

        For example, if test_type is 'proportion_z_test', the kwargs should contain the following keys:
        - successes1: number of successes in the first sample
        - trials1: number of trials in the first sample
        - successes2: number of successes in the second sample
        - trials2: number of trials in the second sample
        - alternative (optional): 'two-sided', 'less', or 'greater'

        :param: test_type (str): The type of hypothesis test to perform ('proportion_z_test', 'fishers_exact_test', or
            'chi_square_test').
        :param: n_folds (int, optional): The number of folds to use for cross-validation (5 default)
        :param: **kwargs: Additional keyword arguments to pass to the cross validate hypothesis test function.

        :return:
            dict: A dictionary containing the average performance metrics across all folds.
        """
        if self.results is None:
            raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

        if n_folds < 2:
            raise ValueError("n_folds must be greater than or equal to 2.")

        # Split the data into n_folds
        fold_size = len(self.results) // n_folds
        folds = [self.results[i:i + fold_size] for i in range(0, len(self.results), fold_size)]

        metrics_list = []

        # Perform hypothesis testing on each fold
        for i in range(n_folds):
            test_data = folds[i]
            train_data = [sample for fold in folds[:i] + folds[i + 1:] for sample in fold]

            # Perform hypothesis testing using the train_data and kwargs

            # Evaluate metrics on the test_data
            metrics = self.calculate_metrics(test_data)
            metrics_list.append(metrics)

        # Calculate average metrics
        avg_metrics = {key: sum([fold[key] for fold in metrics_list]) / n_folds for key in
                       metrics_list[0].keys()}

        return avg_metrics

    def get_results(self):
        if self.results is None:
            raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")
        return self.results


