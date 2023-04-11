# DS5010-Project
Binomail distribution library for class project. \
This README file includes a brief introduction to the module, usage instructions, installation instructions, requirements, and a note on contributing.


# Probability Functions

This Python module provides a set of functions to work with the binomial distribution. It includes the following functions:

1. `validate_parameters(n, p)`: Ensures that the provided parameters are valid for a binomial distribution.
2. `factorial(n)`: Calculates the factorial of a non-negative integer.
3. `binomial_coefficient(n, k)`: Calculates the binomial coefficient (n choose k).
4. `pmf(k, n, p)`: Calculates the probability mass function (PMF) for a binomial distribution.
5. `cdf(x, n, p)`: Calculates the cumulative distribution function (CDF) for a binomial distribution.

### Usage

To use the functions provided in this module, simply import the module and call the desired function with the appropriate parameters:

```python
import binomial_distribution as bd

# Calculate the probability of observing exactly 3 successes in 10 trials with a success probability of 0.5
probability = bd.pmf(3, 10, 0.5)

# Calculate the cumulative probability of observing up to 4 successes in 10 trials with a success probability of 0.5
cumulative_probability = bd.cdf(4, 10, 0.5)

```

### Function Descriptions

1.`validate_parameters(n, p)`

Ensures that the provided parameters are valid for a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: None
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

2.`factorial(n)`

Calculates the factorial of a non-negative integer.

    Input: n (int) - A non-negative integer.
    Output: (int) - The factorial of n.
    Raises: None

3.`binomial_coefficient(n, k)`

Calculates the binomial coefficient (n choose k).

    Input: n (int) - The number of trials; k (int) - The number of successes.
    Output: (int) - The binomial coefficient (n choose k).
    Raises: None

4.`pmf(k, n, p)`

Calculates the probability mass function (PMF) for a binomial distribution.

    Input: k (int) - The number of successes; n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The probability of observing exactly k successes in n trials.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

5.`cdf(x, n, p)`

Calculates the cumulative distribution function (CDF) for a binomial distribution.

    Input: x (int) - The maximum number of successes; n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The cumulative probability of observing up to x successes in n trials.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.
    
### Example Usage

```python
import binomial_distribution as bd

# Calculate the probability of observing exactly 5 heads in 10 coin flips with a fair coin
num_trials = 10
num_successes = 5
probability_success = 0.5

# Probability Mass Function
probability = bd.pmf(num_successes, num_trials, probability_success)
print(f"The probability of observing {num_successes} successes in {num_trials} trials is {probability:.4f}")

# Cumulative Distribution Function
max_successes = 7
cumulative_probability = bd.cdf(max_successes, num_trials, probability_success)
print(f"The cumulative probability of observing up to {max_successes} successes 
```

# Descriptive Statistics for Binomial Distribution

By using the descriptive_statistics.py module, users can easily calculate various descriptive statistics for a binomial distribution. This module provides a convenient way to analyze the distribution's characteristics, such as its mean, variance, standard deviation, mode, skewness, kurtosis, and entropy. The functions are designed to be user-friendly and efficient, making it simple to incorporate them into a wide range of applications.\
The following functions are available in the descriptive_statistics.py module:

### Function Descriptions

1.`validate_parameters(n, p)`

Validates the parameters of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: None
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

2.`mean(n, p)`

Calculates the mean of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The mean of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

3.`variance(n, p)`

Calculates the variance of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The variance of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

4.`standard_deviation(n, p)`

Calculates the standard deviation of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The standard deviation of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

5.`mode(n, p)`

Calculates the mode of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The mode of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

6.`skewness(n, p)`

Calculates the skewness of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The skewness of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

7.`kurtosis(n, p)`

Calculates the kurtosis of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The kurtosis of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

8.`entropy(n, p)`

Calculates the entropy of a binomial distribution.

    Input: n (int) - The number of trials; p (float) - The probability of success.
    Output: (float) - The entropy of the binomial distribution.
    Raises: ValueError if the input parameters are not valid for a binomial distribution.

### Example Usage

```python
import descriptive_statistics as ds

num_trials = 10
probability_success = 0.5

# Mean
binomial_mean = ds.mean(num_trials, probability_success)
print(f"The mean of the binomial distribution is {binomial_mean:.2f}")

# Standard Deviation
binomial_std = ds.standard_deviation(num_trials, probability_deviation(num_trials, probability_success)
print(f"The standard deviation of the binomial distribution is {binomial_std:.2f}")

# Mode
binomial_mode = ds.mode(num_trials, probability_success)
print(f"The mode of the binomial distribution is {binomial_mode}")

# Skewness
binomial_skewness = ds.skewness(num_trials, probability_success)
print(f"The skewness of the binomial distribution is {binomial_skewness:.2f}")

# Kurtosis
binomial_kurtosis = ds.kurtosis(num_trials, probability_success)
print(f"The kurtosis of the binomial distribution is {binomial_kurtosis:.2f}")

# Entropy
binomial_entropy = ds.entropy(num_trials, probability_success)
print(f"The entropy of the binomial distribution is {binomial_entropy:.2f}")
```
