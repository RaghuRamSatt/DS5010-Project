# DS5010-Project
Binomial distribution library for class project. \
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
import Probability as pr

# Calculate the probability of observing exactly 3 successes in 10 trials with a success probability of 0.5
probability = pr.pmf(3, 10, 0.5)

# Calculate the cumulative probability of observing up to 4 successes in 10 trials with a success probability of 0.5
cumulative_probability = pr.cdf(4, 10, 0.5)

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
import Probability as pr

# Calculate the probability of observing exactly 5 heads in 10 coin flips with a fair coin
num_trials = 10
num_successes = 5
probability_success = 0.5

# Probability Mass Function
probability = pr.pmf(num_successes, num_trials, probability_success)
print(f"The probability of observing {num_successes} successes in {num_trials} trials is {probability:.4f}")

# Cumulative Distribution Function
max_successes = 7
cumulative_probability = pr.cdf(max_successes, num_trials, probability_success)
print(f"The cumulative probability of observing up to {max_successes} successes") 
```

# Descriptive Statistics for Binomial Distribution

By using the descriptive_statistics.py module, users can easily calculate various descriptive statistics for a binomial distribution. This module provides a convenient way to analyze the distribution's characteristics, such as its mean, variance, standard deviation, mode, skewness, kurtosis, and entropy. The functions are designed to be user-friendly and efficient, making it simple to incorporate them into a wide range of applications.\
The following functions are available in the descriptive_statistics.py module:

 1. `validate_parameters(n, p)`: Ensures that the provided parameters are valid for a binomial distribution.
 2. `mean(n, p)`: Calculates the mean of a binomial distribution.
 3. `variance(n, p)`: Calculates the variance of a binomial distribution.
 4. `standard_deviation(n, p)`: Calculates the standard deviation of a binomial distribution.
 5. `mode(n, p)`: Calculates the mode of a binomial distribution.
 6. `skewness(n, p)`: Calculates the skewness of a binomial distribution.
 7. `kurtosis(n, p)`: Calculates the kurtosis of a binomial distribution.
 8. `entropy(n, p)`: Calculates the entropy of a binomial distribution.


### Usage

To use the functions provided in this module, simply import the module and call the desired function with the appropriate parameters:

```python
import BinomialStatistics as bs

# Calculate the mean for a binomial distribution with 10 trials and a success probability of 0.5
mean_value = bs.mean(10, 0.5)

# Calculate the standard deviation for a binomial distribution with 10 trials and a success probability of 0.5
std_dev = bs.standard_deviation(10, 0.5)
```

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

# Estimating Parameters and Confidence Intervals for Binomial Distributions

By using the binomial_estimation.py module, users can easily estimate the parameters of a binomial distribution and calculate confidence intervals for the probability of success. This module provides a convenient way to analyze the distribution's characteristics, making it simple to incorporate them into a wide range of applications.

### Functions 

1. `estimate_parameters(sample_data)`: Estimates the number of trials and probability of success using the method of moments based on the provided sample data.
2. `log_likelihood(p, sample_data)`: Calculates the log-likelihood of the sample data given the probability of success (p).
3. `mle_estimate_parameters(sample_data)`: Estimates the number of trials and probability of success using Maximum Likelihood Estimation (MLE) based on the provided sample data.
4. `confidence_interval_normal_approximation(sample_data, confidence_level=0.95)`: Calculates the confidence interval for the probability of success (p) in a binomial distribution using the normal approximation method.
5. `confidence_interval_clopper_pearson(sample_data, confidence_level=0.95)`: Calculates the confidence interval for the probability of success (p) in a binomial distribution using the Clopper-Pearson (exact) method.
6. `confidence_interval_agresti_coull(sample_data, confidence_level=0.95)`: Calculates the confidence interval for the probability of success (p) in a binomial distribution using the Agresti-Coull method.

### Functions Description
1. `estimate_parameters(sample_data)`

Estimates the parameters of a binomial distribution (number of trials and probability of success) using the method of moments based on sample data.

    Input:
        sample_data:  (list)- A list of binomial samples with the same number of trials and success probability.
        Output: (tuple) - A tuple containing the estimated number of trials (int) and the estimated probability of success (float).
        Raises: ValueError - If the sample data is empty or if the sample variance is zero.
        
2. `log_likelihood(p, sample_data)`

Calculates the log-likelihood of the sample data given the probability of success (p).

    Input:
        p (float) - The probability of success.
        sample_data (list) - A list of binomial samples with the same number of trials and success probability.
    Output:
        (float) - The log-likelihood of the sample data given p.
        
3. `mle_estimate_parameters(sample_data)`

Estimates the parameters of a binomial distribution (number of trials and probability of success) using Maximum Likelihood Estimation (MLE) based on sample data.

    Input:
        sample_data (list) - A list of binomial samples with the same number of trials and success probability.
    Output:
        (tuple) - A tuple containing the estimated number of trials (int) and the estimated probability of success (float).
    Raises:
        ValueError - If the sample data is empty.
        
4. `confidence_interval_normal_approximation(sample_data, confidence_level=0.95)`

Calculates the confidence interval for the probability of success (p) in a binomial distribution using the normal approximation method. The function uses the normal approximation method, which might not be accurate for small sample sizes or extreme probabilities (close to 0 or 1).

    Input:
        sample_data (list) - A list of binomial samples with the same number of trials and success probability.
        confidence_level (float, optional): The desired confidence level (default is 0.95).
    Output:
        (tuple) - A tuple containing the lower and upper bounds of the confidence interval for p.
    Raises:
        ValueError - If the sample data is empty.
        
5. `confidence_interval_clopper_pearson(sample_data, confidence_level=0.95)`

Calculates the confidence interval for the probability of success (p) in a binomial distribution using the Clopper-Pearson (exact) method.

    Input:
        sample_data (list) -  A list of binomial samples with the same number of trials and success probability.
        confidence_level (float, optional): The desired confidence level (default is 0.95).
    Output:
        (tuple) - A tuple containing the lower and upper bounds of the confidence interval for p.
    Raises:
        ValueError - If the sample data is empty.
        
6. `confidence_interval_agresti_coull(sample_data, confidence_level=0.95)`

Calculates the confidence interval for the probability of success (p) in a binomial distribution using the Agresti-Coull method.

    Input:
        sample_data (list) - A list of binomial samples with the same number of trials and success probability.
        confidence_level (float, optional): The desired confidence level (default is 0.95).
    Output:
        (tuple) - A tuple containing the lower and upper bounds of the confidence interval for p.
     Raises:
        ValueError - If the sample data is empty.
        
        
### Examples

``` python 
import binomial_estimation as be

# Sample data
sample_data = [4, 5, 6, 4, 5, 7, 5, 6, 5, 4]

# Estimate parameters using the method of moments
n_estimate, p_estimate = be.estimate_parameters(sample_data)
print("Method of moments estimates:")
print("n =", n_estimate)
print("p =", p_estimate)

# Estimate parameters using Maximum Likelihood Estimation (MLE)
n_estimate_mle, p_estimate_mle = be.mle_estimate_parameters(sample_data)
print("MLE estimates:")
print("n =", n_estimate_mle)
print("p =", p_estimate_mle)

# Calculate confidence intervals using various methods
ci_normal = be.confidence_interval_normal_approximation(sample_data)
ci_clopper_pearson = be.confidence_interval_clopper_pearson(sample_data)
ci_agresti_coull = be.confidence_interval_agresti_coull(sample_data)

print("Confidence intervals:")
print("Normal approximation:", ci_normal)
print("Clopper-Pearson:", ci_clopper_pearson)
print("Agresti-Coull:", ci_agresti_coull)
```
