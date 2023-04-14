#!/usr/bin/env python
# coding: utf-8

# In[1]:

import math

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("Matplotlib is required. Please install it using 'pip install matplotlib'.")

from descriptive_statistics import standard_deviation
from Probability import (pmf, cdf)


def validate_parameters(n, p):
    """
    To ensure that the provided parameters are valid for a binomial distribution.

    :param n: (int) A non - negative integer
    :param p: (float) The probability of success

    :raises: (ValueError): If the input parameters are not valid for a binomial distribution.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")
    if not (0 <= p <= 1):
        # if not (math.isclose(p, 0) or math.isclose(p, 1) or (0 < p < 1)):
        # math.is close function to handle floating-point comparisons for the probability p.
        raise ValueError("p must be a probability value between 0 and 1 (inclusive).")


def plot_pmf(n, p, chart_type='line', show_error_bars=False):
    """
    Plots the probability mass function (PMF) of the binomial distribution.

    :param:
    n (int): The number of trials.
    p (float): The probability of success for each trial.
    chart_type (str, optional): The type of chart to plot. Options: 'line' (default) or 'bar'.
    show_error_bars (bool, optional): Whether to show error bars on the plot. Default is False.

    :raises:
    ValueError: If n is not a non-negative integer or if p is not a float between 0 and 1, inclusive.
    ImportError: If matplotlib is not installed.
    """
    validate_parameters(n, p)

    x_values = list(range(n + 1))
    y_values = [pmf(k, n, p) for k in x_values]

    if show_error_bars:
        std_dev = standard_deviation(n, p)
        error_values = [std_dev * math.sqrt(y * (1 - y) / n) for y in y_values]
        plt.errorbar(x_values, y_values, yerr=error_values, fmt='o-', capsize=5)
    else:
        if chart_type == 'bar':
            plt.bar(x_values, y_values)
        else:
            plt.plot(x_values, y_values)

    plt.title('Binomial PMF')
    plt.xlabel('k')
    plt.ylabel('Probability')
    plt.show()


def plot_cdf(n, p, chart_type='line', show_error_bars=False):
    """
    Plots the cumulative distribution function (CDF) of the binomial distribution.

    :param:
    n (int): The number of trials.
    p (float): The probability of success for each trial.
    chart_type (str, optional): The type of chart to plot. Options: 'line' (default) or 'bar'.
    show_error_bars (bool, optional): Whether to show error bars on the plot. Default is False.

    :raises:
    ValueError: If n is not a non-negative integer or if p is not a float between 0 and 1, inclusive.
    ImportError: If matplotlib is not installed.
    """
    validate_parameters(n, p)

    x_values = list(range(n + 1))
    y_values = [cdf(k, n, p) for k in x_values]

    if show_error_bars:
        std_dev = standard_deviation(n, p)
        error_values = [std_dev * math.sqrt(y * (1 - y) / n) for y in y_values]
        plt.errorbar(x_values, y_values, yerr=error_values, fmt='o-', capsize=5)
    else:
        if chart_type == 'bar':
            plt.bar(x_values, y_values)
        else:
            plt.plot(x_values, y_values)

    plt.title('Binomial CDF')
    plt.xlabel('k')
    plt.ylabel('Cumulative Probability')
    plt.show()

# In[ ]:
