import numpy as np
import scipy.stats as stats


def proportion_z_test(successes1, trials1, successes2, trials2, alternative='two-sided'):
    """
    Perform a proportion z-test to compare two binomial proportions. This function performs a proportion z-test to
    compare two binomial proportions. It takes the number of successes and total trials for two groups, as well as
    the alternative hypothesis, and returns the p-value of the test.

    :param successes1: (int) The number of successes in group 1
    :param trials1: (int) The total number of trials in group 1
    :param successes2: (int) The number of successes in group 2
    :param trials2: (int) The total number of trials in group 2
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')

    :return: (float) The p-value of the test

    """
    if not all(isinstance(x, int) for x in [successes1, trials1, successes2, trials2]):
        raise ValueError("All input values for successes and trials must be integers.")
    if trials1 == 0 or trials2 == 0:
        raise ValueError("Both trials1 and trials2 must be greater than 0.")
    if alternative not in ['two-sided', 'greater', 'less']:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")

    p1 = successes1 / trials1
    p2 = successes2 / trials2
    pooled_p = (successes1 + successes2) / (trials1 + trials2)
    standard_error = np.sqrt(pooled_p * (1 - pooled_p) * (1 / trials1 + 1 / trials2))
    z_stat = (p1 - p2) / standard_error

    # print("pooled_p:", pooled_p)
    # print("se:", standard_error)
    # print("z_stat", z_stat)

    if alternative == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")
    return p_value


def power_analysis_binomial_proportions(p1, p2, alpha=0.05, power=0.8, alternative='two-sided', ratio=1):
    """
    Perform a power analysis for a proportion z-test comparing two binomial proportions to determine the required
    sample size. This function performs a power analysis for a proportion z-test, comparing two binomial proportions
    to determine the required sample size. It takes the true proportions for two groups, the desired significance
    level, the desired statistical power, the alternative hypothesis, and the ratio of sample sizes between the
    groups as input and returns the required sample size for group 1.

    :param p1: (float) The true proportion in group 1
    :param p2: (float) The true proportion in group 2
    :param alpha: (float) The desired significance level (default is 0.05)
    :param power: (float) The desired statistical power (power is 0.8)
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')
    :param ratio: (float) The ratio of sample sizes between group 2 and group 1 (default is 1)

    :return: (int) The required sample size for group 1
    """
    if not all(isinstance(x, (int, float)) for x in [p1, p2, alpha, power, ratio]):
        raise ValueError("All input values for p1, p2, alpha, power, and ratio must be numbers (integers or floats).")
    if not (0 <= p1 <= 1) or not (0 <= p2 <= 1) or not (0 <= alpha <= 1) or not (0 <= power <= 1):
        raise ValueError("p1, p2, alpha, and power must be between 0 and 1 (inclusive).")

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
    Perform Fisher's exact test for equality of two binomial proportions. This function performs Fisher's exact test
    for equality of two binomial proportions. It takes the number of successes and total trials for two groups,
    as well as the alternative hypothesis, and returns the p-value for the test.

    :param success1: (int) The number of successes in group 1
    :param total1: (int) The total number of trials in group 1
    :param success2: (int) The number of successes in group 2
    :param total2: (int) The total number of trials in group 2
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')

    :return: (float) The p-value for the test
    """
    if not all(isinstance(x, int) for x in [success1, total1, success2, total2]):
        raise ValueError("All input values for success1, total1, success2, and total2 must be integers.")
    if total1 < 0 or total2 < 0:
        raise ValueError('trials1 and trials2 must be non-negative')
    if total1 == 0 or total2 == 0:
        return np.nan, np.nan
    if alternative not in ['two-sided', 'greater', 'less']:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")

    oddsratio, p_value = stats.fisher_exact([[success1, total1 - success1], [success2, total2 - success2]],
                                            alternative=alternative)
    return p_value


def chi_square_test(binomial_data, expected_proportions=None):
    """
    Perform a chi-square test for the equality of multiple binomial proportions. This function performs a chi-square
    test for the equality of multiple binomial proportions. It takes a list of tuples containing the number of
    successes and total trials for each group, and optionally, a list of expected proportions for each group. If not
    provided, the test assumes equal proportions. The function returns the p-value for the test.

    :param binomial_data: (list) A list of tuples containing the number of successes and total trials for each group
    :param expected_proportions: (list, optional) A list of expected proportions for each group. If not provided, the
                                  test will assume equal proportions.

    :return: (float) The p-value for the test
    """
    if not isinstance(binomial_data, list) or not all(
            isinstance(x, tuple) and len(x) == 2 and all(isinstance(y, int) for y in x) for x in binomial_data):
        raise ValueError("binomial_data must be a list of tuples, each containing two integers.")
    if expected_proportions is not None:
        if not isinstance(expected_proportions, list) or not all(
                isinstance(x, (int, float)) for x in expected_proportions):
            raise ValueError("expected_proportions must be a list of numbers (integers or floats).")

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
    Perform a G-test for goodness-of-fit for binomial data. This function performs a G-test for goodness-of-fit for
    binomial data. It takes a list of tuples containing the number of successes and total trials for each group,
    and optionally, a list of expected proportions for each group. If not provided, the test assumes equal
    proportions. The function returns the p-value for the test.

    :param binomial_data: (list) A list of tuples containing the number of successes and total trials for each group
    :param expected_proportions: (list, optional) A list of expected proportions for each group. If not provided, the
                                  test will assume equal proportions.

    :return: (float) The p-value for the test
    """
    if not isinstance(binomial_data, list) or not all(
            isinstance(x, tuple) and len(x) == 2 and all(isinstance(y, int) for y in x) for x in binomial_data):
        raise ValueError("binomial_data must be a list of tuples, each containing two integers.")
    if expected_proportions is not None:
        if not isinstance(expected_proportions, list) or not all(
                isinstance(x, (int, float)) for x in expected_proportions):
            raise ValueError("expected_proportions must be a list of numbers (integers or floats).")
        if not (sum(expected_proportions) == 1 and all(0 <= x <= 1 for x in expected_proportions)):
            raise ValueError("expected_proportions must be non-negative and sum up to 1.")

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


def proportion_confidence_interval(success, trials, alpha=0.05):
    """
    Calculate the confidence interval for a binomial proportion.

    :param success: (int) The number of successes
    :param trials: (int) The total number of trials
    :param alpha: (float) The desired significance level (default is 0.05)

    :return: (tuple) A tuple containing the lower and upper bounds of the confidence interval
    """
    if not all(isinstance(x, int) for x in [success, trials]):
        raise ValueError("success and trials must be integers.")
    if not (0 <= alpha <= 1):
        raise ValueError("alpha must be between 0 and 1 (inclusive).")

    p = success / trials
    z_alpha = stats.norm.ppf(1 - alpha / 2)
    standard_error = np.sqrt(p * (1 - p) / trials)

    lower_bound = p - z_alpha * standard_error
    upper_bound = p + z_alpha * standard_error

    return lower_bound, upper_bound


def cohen_h_effect_size(p1, p2):
    """
    Calculate Cohen's h effect size for proportions.

    :param p1: (float) The proportion for group 1
    :param p2: (float) The proportion for group 2

    :return: (float) Cohen's h effect size
    """
    if not all(isinstance(x, (int, float)) for x in [p1, p2]):
        raise ValueError("p1 and p2 must be numbers (integers or floats).")

    h = 2 * np.arcsin(np.sqrt(p1)) - 2 * np.arcsin(np.sqrt(p2))

    return h


def continuity_corrected_proportion_z_test(successes1, trials1, successes2, trials2, alternative='two-sided'):
    """
    Perform a continuity-corrected proportion z-test to compare two binomial proportions.

    :param successes1: (int) The number of successes in group 1
    :param trials1: (int) The total number of trials in group 1
    :param successes2: (int) The number of successes in group 2
    :param trials2: (int) The total number of trials in group 2
    :param alternative: (str) The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')

    :return: (float) The p-value of the test
    """
    if not all(isinstance(x, int) for x in [successes1, trials1, successes2, trials2]):
        raise ValueError("All input values for successes and trials must be integers.")
    if alternative not in ['two-sided', 'greater', 'less']:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")

    p1 = successes1 / trials1
    p2 = successes2 / trials2
    pooled_p = (successes1 + successes2) / (trials1 + trials2)
    standard_error = np.sqrt(pooled_p * (1 - pooled_p) * (1 / trials1 + 1 / trials2))

    # Apply continuity correction
    correction = 1 / (2 * trials1) - 1 / (2 * trials2)
    z_stat = (p1 - p2 - np.sign(p1 - p2) * correction) / standard_error

    if alternative == 'two-sided':
        p_value = (2 * (1 - stats.norm.cdf(abs(z_stat))))
    elif alternative == 'greater':
        p_value = 1 - stats.norm.cdf(z_stat)
    elif alternative == 'less':
        p_value = stats.norm.cdf(z_stat)
    else:
        raise ValueError("Invalid alternative hypothesis. Choose from 'two-sided', 'greater', or 'less'.")

    return p_value
