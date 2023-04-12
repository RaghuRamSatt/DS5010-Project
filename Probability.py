import math


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


def factorial(n):
    """
    Calculate the factorial of a non-negative integer.Using an iterative approach instead of recursion to avoid the risk
    of reaching Python's maximum recursion depth for large inputs.

    :param n: (int) A non-negative integer

    :return: (int) The factorial of n
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def binomial_coefficient(n, k):
    """
    Calculate the binomial coefficient (n choose k). Optimized version that uses the multiplicative formula, which is
    more efficient for larger inputs.

    :param n: (int) The number of trials
    :param k: (int) The number of successes

    :return: (int) The binomial coefficient (n choose k)
    """
    if k > n - k:
        k = n - k
    result = 1
    for i in range(1, k + 1):
        result *= (n - k + i)
        result //= i
    return result


def pmf(k, n, p):
    """
    Calculate the probability mass function (PMF) for a binomial distribution.

    :param k: (int) The number of successes
    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The probability of observing exactly k successes in n trails
    """
    validate_parameters(n, p)
    if not (0 <= k <= n):
        raise ValueError("k must be between 0 and n (inclusive).")
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))  # math.comb makes the code more concise and efficient


def cdf(x, n, p):
    """
    Calculate the probability mass function (CDF) for a binomial distribution.

    :param x: (int) The maximum number of successes
    :param n: (int) The number of trials
    :param p: (float) The probability of success

    :return: (float) The cumulative probability of observing up to x successes in n trials
    """
    validate_parameters(n, p)
    if not (0 <= x <= n):
        raise ValueError("x must be between 0 and n (inclusive).")
    cumulative_probability = 0
    for k in range(x + 1):
        cumulative_probability += pmf(k, n, p)
    return cumulative_probability
