import numpy as np
import scipy.stats as stats


def proportion_z_test(successes1, trials1, successes2, trials2, alternative='two-sided'):
    """
    Perform a proportion z-test to compare two binomial proportions.

    :param successes1: (int) The number of successes in group 1
    :param trials1: (int) The total number of trials in group 1
    :param successes2: (int) The number of successes in group 2
    :param trials2: (int) The total number of trials in group 2
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')

    :return: (float) The p-value of the test
    """
    p1 = successes1 / trials1
    p2 = successes2 / trials2
    pooled_p = (successes1 + successes2) / (trials1 + trials2)
    standard_error = np.sqrt(pooled_p * (1 - pooled_p) * (1 / trials1 + 1 / trials2))
    z_stat = (p1 - p2) / standard_error

    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")


def power_analysis_binomial_proportions(p1, p2, alpha, power, alternative='two-sided', ratio=1):
    """
    Perform a power analysis for a proportion z-test comparing two binomial proportions to determine the required sample
    size.

    :param p1: (float) The true proportion in group 1
    :param p2: (float) The true proportion in group 2
    :param alpha: (float) The desired significance level
    :param power: (float) The desired statistical power
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')
    :param ratio: (float) The ratio of sample sizes between group 2 and group 1 (default is 1)

    :return: (int) The required sample size for group 1
    """
    pooled_p = (p1 + ratio * p2) / (1 + ratio)
    standard_error = np.sqrt(pooled_p * (1 - pooled_p) * (1 + 1 / ratio))

    if alternative == 'two-sided':
        z_alpha = stats.norm.ppf(1 - alpha / 2)
    elif alternative == 'greater' or alternative == 'less':
        z_alpha = stats.norm.ppf(1 - alpha)
    else:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")

    z_power = stats.norm.ppf(power)
    sample_size1 = ((z_alpha + z_power) * standard_error / (p1 - p2)) ** 2

    return int(np.ceil(sample_size1))


def fishers_exact_test(success1, total1, success2, total2, alternative='two-sided'):
    """
    Perform Fisher's exact test for equality of two binomial proportions.

    :param success1: (int) The number of successes in group 1
    :param total1: (int) The total number of trials in group 1
    :param success2: (int) The number of successes in group 2
    :param total2: (int) The total number of trials in group 2
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')

    :return: (float) The p-value for the test
    """
    oddsratio, p_value = stats.fisher_exact([[success1, total1 - success1], [success2, total2 - success2]], alternative=alternative)
    return p_value


def chi_square_test(binomial_data, expected_proportions=None):
    """
    Perform a chi-square test for the equality of multiple binomial proportions.

    :param binomial_data: (list) A list of tuples containing the number of successes and total trials for each group
    :param expected_proportions: (list, optional) A list of expected proportions for each group. If not provided, the
                                  test will assume equal proportions.

    :return: (float) The p-value for the test
    """
    observed_successes = np.array([x[0] for x in binomial_data])
    total_trials = np.array([x[1] for x in binomial_data])

    if expected_proportions is None:
        expected_proportions = np.full(len(binomial_data), 1 / len(binomial_data))

    if len(expected_proportions) != len(binomial_data):
        raise ValueError("Number of expected proportions must match the number of binomial data groups.")

    total_successes = np.sum(observed_successes)
    expected_successes = total_successes * np.array(expected_proportions)
    chi_square_statistic = np.sum(((observed_successes - expected_successes) ** 2) / expected_successes)
    degrees_of_freedom = len(binomial_data) - 1
    p_value = 1 - stats.chi2.cdf(chi_square_statistic, degrees_of_freedom)

    return p_value


def g_test_goodness_of_fit(binomial_data, expected_proportions=None):
    """
    Perform a G-test for goodness-of-fit for binomial data.

    :param binomial_data: (list) A list of tuples containing the number of successes and total trials for each group
    :param expected_proportions: (list, optional) A list of expected proportions for each group. If not provided, the
                                  test will assume equal proportions.

    :return: (float) The p-value for the test
    """
    observed_successes = np.array([x[0] for x in binomial_data])
    total_trials = np.array([x[1] for x in binomial_data])

    if expected_proportions is None:
        expected_proportions = np.full(len(binomial_data), 1 / len(binomial_data))

    if len(expected_proportions) != len(binomial_data):
        raise ValueError("Number of expected proportions must match the number of binomial data groups.")

    total_successes = np.sum(observed_successes)
    expected_successes = total_successes * np.array(expected_proportions)
    g_statistic = 2 * np.sum(observed_successes * np.log(observed_successes / expected_successes))
    degrees_of_freedom = len(binomial_data) - 1
    p_value = 1 - stats.chi2.cdf(g_statistic, degrees_of_freedom)

    return p_value

