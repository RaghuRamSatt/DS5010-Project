import numpy as np
import math
from scipy.optimize import minimize_scalar
from scipy.stats import beta
from Probability import pmf
from scipy.stats import norm


def estimate_parameters(sample_data):
    """
    Estimate the parameters of a binomial distribution (number of trials and probability of success)
    using the method of moments based on sample data.

    :param sample_data: (list) A list of binomial samples with the same number of trials and success probability.

    :return: (tuple) A tuple containing the estimated number of trials (int) and the estimated probability of success
    (float).
    """
    if not sample_data:
        raise ValueError("Sample data cannot be empty.")

    sample_size = len(sample_data)
    sample_mean = sum(sample_data) / sample_size
    sample_variance = sum((x - sample_mean) ** 2 for x in sample_data) / sample_size

    if sample_variance == 0:
        raise ValueError("Sample variance cannot be zero. Provide a more varied sample data.")

    p_estimate = 1 - (sample_variance / sample_mean)
    n_estimate = round(sample_mean / p_estimate)

    return n_estimate, p_estimate


def log_likelihood(p, sample_data):
    """
    Calculate the log-likelihood of the sample data given the probability of success (p).

    :param p: (float) The probability of success
    :param sample_data: (list) A list of binomial samples with the same number of trials and success probability.

    :return: (float) The log-likelihood of the sample data given p
    """

    n = len(sample_data)
    # log_likelihood_value = np.sum(np.log(pmf(x, max(sample_data), p)) for x in sample_data)
    log_likelihood_value = sum(np.log(pmf(x, max(sample_data), p)) for x in sample_data)
    return log_likelihood_value


def mle_estimate_parameters(sample_data):
    """
    Estimate the parameters of a binomial distribution (number of trials and probability of success)
    using Maximum Likelihood Estimation (MLE) based on sample data.

    :param sample_data: (list) A list of binomial samples with the same number of trials and success probability

    :return: (tuple) A tuple containing the estimated number of trials (int) and the estimated probability of success
    (float)
    """
    if not sample_data:
        raise ValueError("Sample data cannot be empty.")

    n_estimate = max(sample_data)
    result = minimize_scalar(lambda p: -log_likelihood(p, sample_data), bounds=(0, 1), method='bounded')
    p_estimate = result.x

    return n_estimate, p_estimate


def confidence_interval_normal_approximation(sample_data, confidence_level=0.95):
    """
    Calculate the confidence interval for the probability of success (p) in a binomial distribution
    using the normal approximation method. The function uses the normal approximation method. Please note that the
    normal approximation method might not be accurate for small sample sizes or extreme probabilities (close to 0 or 1).

    :param sample_data: (list) A list of binomial samples with the same number of trials and success probability
    :param confidence_level: (float, optional) The desired confidence level (default is 0.95)

    :return: (tuple)  A tuple containing the lower and upper bounds of the confidence interval for p
    """
    if not sample_data:
        raise ValueError("Sample data cannot be empty.")

    n = len(sample_data)
    _, p_estimate = estimate_parameters(sample_data)
    standard_error = math.sqrt(p_estimate * (1 - p_estimate) / n)

    # z_score = abs(np.percentile(np.random.standard_normal(100000), (1 - confidence_level) / 2 + confidence_level *
    # 100))
    z_score = norm.ppf(1 - (1 - confidence_level) / 2)
    margin_of_error = z_score * standard_error

    lower_bound = max(0, p_estimate - margin_of_error)
    upper_bound = min(1, p_estimate + margin_of_error)

    return lower_bound, upper_bound


def confidence_interval_clopper_pearson(sample_data, confidence_level=0.95):
    """
    Calculate the confidence interval for the probability of success (p) in a binomial distribution
    using the Clopper-Pearson (exact) method.

    :param sample_data: (list) A list of binomial samples with the same number of trials and success probability
    :param confidence_level: (float, optional) The desired confidence level (default is 0.95)

    :return: (tuple) A tuple containing the lower and upper bounds of the confidence interval for p
    """
    if not sample_data:
        raise ValueError("Sample data cannot be empty.")

    n = len(sample_data)
    n_trials, _ = estimate_parameters(sample_data)
    total_successes = sum(sample_data)

    alpha = 1 - confidence_level
    lower_bound = beta.ppf(alpha / 2, total_successes, n * n_trials - total_successes + 1)
    upper_bound = beta.ppf(1 - alpha / 2, total_successes + 1, n * n_trials - total_successes)

    return lower_bound, upper_bound


def confidence_interval_agresti_coull(sample_data, confidence_level=0.95):
    """
    Calculate the confidence interval for the probability of success (p) in a binomial distribution
    using the Agresti-Coull method.

    :param sample_data: (list)  A list of binomial samples with the same number of trials and success probability
    :param confidence_level: (float, optional) The desired confidence level (default is 0.95)

    :return: (tuple) A tuple containing the lower and upper bounds of the confidence interval for p
    """
    if not sample_data:
        raise ValueError("Sample data cannot be empty.")

    n = len(sample_data)
    _, p_estimate = estimate_parameters(sample_data)
    z_score = abs(np.percentile(np.random.standard_normal(100000), (1 - confidence_level) / 2 + confidence_level * 100))

    adjusted_n = n + z_score ** 2
    adjusted_p = (sum(sample_data) + (z_score ** 2) / 2) / adjusted_n

    standard_error = math.sqrt(adjusted_p * (1 - adjusted_p) / adjusted_n)
    margin_of_error = z_score * standard_error

    lower_bound = max(0, adjusted_p - margin_of_error)
    upper_bound = min(1, adjusted_p + margin_of_error)

    return lower_bound, upper_bound
