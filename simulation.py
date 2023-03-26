import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hypothesis_testing import proportion_z_test, fishers_exact_test, chi_square_test


def calculate_performance_metrics(true_positives, false_positives, true_negatives, false_negatives):
    sensitivity = true_positives / (true_positives + false_negatives)
    specificity = true_negatives / (true_negatives + false_positives)
    positive_predictive_value = true_positives / (true_positives + false_positives)
    negative_predictive_value = true_negatives / (true_negatives + false_negatives)
    accuracy = (true_positives + true_negatives) / (
            true_positives + false_positives + true_negatives + false_negatives)

    return {
        'sensitivity': sensitivity,
        'specificity': specificity,
        'positive_predictive_value': positive_predictive_value,
        'negative_predictive_value': negative_predictive_value,
        'accuracy': accuracy
    }


class BinomialSimulation:
    def __init__(self, n_trials, p_success, n_experiments):
        self.n_trials = n_trials
        self.p_success = p_success
        self.n_experiments = n_experiments
        self.results = None

    def run_simulation(self):
        self.results = np.random.binomial(self.n_trials, self.p_success, size=self.n_experiments)

    def plot_histogram(self, bins=None):
        if self.results is None:
            raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

        plt.figure()
        sns.histplot(self.results, kde=False, bins=bins)
        plt.title("Histogram of Successes in Binomial Experiments")
        plt.xlabel("Number of Successes")
        plt.ylabel("Frequency")
        plt.show()

    def plot_success_probability_evolution(self, window_size=10):
        if self.results is None:
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


def cross_validate_hypothesis_testing(self, test_type, n_folds=5, **kwargs):
    if self.results is None:
        raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

    if n_folds < 2:
        raise ValueError("n_folds must be greater than or equal to 2.")

    # Split the data into n_folds
    fold_size = len(self.results) // n_folds
    folds = [self.results[i:i + fold_size] for i in range(0, len(self.results), fold_size)]

    performance_metrics = []

    # Perform hypothesis testing on each fold
    for i in range(n_folds):
        test_data = folds[i]
        train_data = [sample for fold in folds[:i] + folds[i + 1:] for sample in fold]

        # Perform hypothesis testing using the train_data and kwargs

        # Evaluate performance metrics on the test_data
        metrics = self.calculate_performance_metrics(...)  # Calculate metrics using the test_data
        performance_metrics.append(metrics)

    # Calculate average performance metrics
    avg_metrics = {key: sum([fold[key] for fold in performance_metrics]) / n_folds for key in
                   performance_metrics[0].keys()}

    return avg_metrics


def plot_success_distribution(self):
    if self.results is None:
        raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

    successes = [result['successes'] for result in self.results]
    unique_successes = sorted(list(set(successes)))
    frequencies = [successes.count(s) for s in unique_successes]

    plt.bar(unique_successes, frequencies)
    plt.xlabel('Number of Successes')
    plt.ylabel('Frequency')
    plt.title('Distribution of Successes in Simulated Experiments')
    plt.show()


def plot_success_probabilities_evolution(self):
    if self.results is None:
        raise ValueError("Simulation has not been run. Call 'run_simulation()' first.")

    success_probabilities = [result['success_probability'] for result in self.results]
    experiment_number = list(range(1, len(self.results) + 1))

    plt.plot(experiment_number, success_probabilities)
    plt.xlabel('Experiment Number')
    plt.ylabel('Success Probability')
    plt.title('Evolution of Success Probabilities in Simulated Experiments')
    plt.show()
