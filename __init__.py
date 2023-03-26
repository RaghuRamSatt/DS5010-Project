from Probability import validate_parameters, factorial, binomial_coefficient, pmf, cdf
from descriptive_statistics import (
    validate_parameters,
    mean,
    variance,
    standard_deviation,
    mode,
    skewness,
    kurtosis,
    entropy
)
from random_sampling import bernoulli_trial, binomial_sample, generate_binomial_samples
from parameter_estimation import (
    estimate_parameters,
    log_likelihood,
    mle_estimate_parameters,
    confidence_interval_normal_approximation,
    confidence_interval_clopper_pearson,
    confidence_interval_agresti_coull
)
from hypothesis_testing import (
    proportion_z_test,
    power_analysis_binomial_proportions,
    fishers_exact_test,
    chi_square_test,
    g_test_goodness_of_fit
)
# Example usage
n = 10
p = 0.5
k = 5
x = 6

print(f"PMF for k={k}, n={n}, p={p}: {pmf(k, n, p)}")
print(f"CDF for x={x}, n={n}, p={p}: {cdf(x, n, p)}")

print(f"Mean: {mean(n, p)}")
print(f"Variance: {variance(n, p)}")
print(f"Standard Deviation: {standard_deviation(n, p)}")
print(f"Mode: {mode(n, p)}")
print(f"Skewness: {skewness(n, p)}")

sample_size = 1000
samples = generate_binomial_samples(sample_size, n, p)
print(f"Generated {sample_size} samples for n={n}, p={p}:")
print(samples)