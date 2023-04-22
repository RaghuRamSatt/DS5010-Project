from Probability import *

from descriptive_statistics import *

from random_sampling import *
from parameter_estimation import *

from hypothesis_testing import *


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