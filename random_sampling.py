import random
from Probability import validate_parameters


def bernoulli_trial(p):
    """
    Simulate a single Bernoulli trial with success probability p.

    :param p: (float) The probability of success.

    :return: (int) 1 if the trial is successful, 0 otherwise
    """
    return 1 if random.random() < p else 0


def binomial_sample(n, p):
    """
    Simulate a single binomial experiment with n trials and success probability p.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (int) The number of successful trials in the binomial experiment
    """
    return sum(bernoulli_trial(p) for _ in range(n))


def generate_binomial_samples(sample_size, n, p, seed=None):
    """
    Generate a specified number of binomial samples with parameters n and p

    :param sample_size: (int) The number of samples to generate
    :param n: (int) The number of trials in each binomial experiment
    :param p: (float) The probability of success in each trial
    :param seed: (int, optional)  A seed value for the random number generator, if reproducibility is desired

    :return: (list) A list of binomial samples with the given parameters
    """
    validate_parameters(n, p)
    if seed is not None:
        random.seed(seed)
    return [binomial_sample(n, p) for _ in range(sample_size)]



