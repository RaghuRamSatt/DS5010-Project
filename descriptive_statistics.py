import math
from Probability import pmf


def validate_parameters(n, p):
    """
    To ensure that the provided parameters are valid for a binomial distribution.

    :param n: (int) A non - negative integer
    :param p: (float) The probability of success

    :return: (ValueError) If the input parameters are not valid for a binomial distribution.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    if not (0 <= p <= 1):
        # if not (math.isclose(p, 0) or math.isclose(p, 1) or (0 < p < 1)):
        # math.is close function to handle floating-point comparisons for the probability p.
        raise ValueError("p must be a probability value between 0 and 1 (inclusive).")


def mean(n, p):
    """
    Calculate the mean of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The mean of the binomial distribution
    """
    validate_parameters(n, p)
    return n * p


def variance(n, p):
    """
    Calculate the variance of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The variance of the binomial distribution
    """
    validate_parameters(n, p)
    q = 1 - p
    return n * p * q


def standard_deviation(n, p):
    """
    Calculate the standard deviation of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The standard deviation of the binomial distribution
    """
    validate_parameters(n, p)
    return (variance(n, p))**0.5


def mode(n, p):
    """
     Calculate the mode of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The mode of the binomial distribution
    """
    validate_parameters(n, p)
    q = 1 - p
    return int((n + 1) * p) if p != 1 else n


def skewness(n, p):
    """
    Calculate the skewness of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The skewness of the binomial distribution.
    """
    validate_parameters(n, p)
    q = 1 - p
    return (q - p) / (n * p * q)**0.5


def kurtosis(n, p):
    """
    Calculate the kurtosis of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The kurtosis of the binomial distribution.
    """
    validate_parameters(n, p)
    q = 1 - p
    return (1 - 6 * p * q) / (n * p * q)


def entropy(n, p):
    """
    Calculate the entropy of a binomial distribution.

    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The entropy of the binomial distribution.
    """
    validate_parameters(n, p)

    if math.isclose(p, 0) or math.isclose(p, 1):
        return 0

    entropy_sum = 0
    for k in range(n + 1):
        prob = pmf(k, n, p)
        if prob > 0:
            entropy_sum += prob * math.log2(prob)

    return -entropy_sum
