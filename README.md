# DS5010-Project
Binomial distribution library for class project. \
This README file includes a brief introduction to the module, usage instructions, installation instructions, requirements, and a note on contributing.


# Probability module

This Python module provides a set of functions to work with the binomial distribution. It includes the following functions:

1. `validate_parameters(n, p)`: Ensures that the provided parameters are valid for a binomial distribution.
2. `factorial(n)`: Calculates the factorial of a non-negative integer.
3. `binomial_coefficient(n, k)`: Calculates the binomial coefficient (n choose k).
4. `pmf(k, n, p)`: Calculates the probability mass function (PMF) for a binomial distribution.
5. `cdf(x, n, p)`: Calculates the cumulative distribution function (CDF) for a binomial distribution.

<!-- ### Usage

To use the functions provided in this module, simply import the module and call the desired function with the appropriate parameters:

```python
import Probability as pr

# Calculate the probability of observing exactly 3 successes in 10 trials with a success probability of 0.5
probability = pr.pmf(3, 10, 0.5)

# Calculate the cumulative probability of observing up to 4 successes in 10 trials with a success probability of 0.5
cumulative_probability = pr.cdf(4, 10, 0.5)

``` -->

### Function Descriptions

1.`validate_parameters(n, p)`

Ensures that the provided parameters are valid for a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            None
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

2.`factorial(n)`

Calculates the factorial of a non-negative integer.

    Input: 
            n (int) - A non-negative integer.
    Output: 
            (int) - The factorial of n.
    Raises: 
            None

3.`binomial_coefficient(n, k)`

Calculates the binomial coefficient (n choose k).

    Input: 
            n (int) - The number of trials
            k (int) - The number of successes.
    Output: 
            (int) - The binomial coefficient (n choose k).
    Raises: 
            None

4.`pmf(k, n, p)`

Calculates the probability mass function (PMF) for a binomial distribution.

    Input: 
            k (int) - The number of successes
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The probability of observing exactly k successes in n trials.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

5.`cdf(x, n, p)`

Calculates the cumulative distribution function (CDF) for a binomial distribution.

    Input: 
            x (int) - The maximum number of successes
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The cumulative probability of observing up to x successes in n trials.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.
    
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

# Descriptive Statistics module

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


<!-- ### Usage

To use the functions provided in this module, simply import the module and call the desired function with the appropriate parameters:

```python
import descriptive_statistics as ds

# Calculate the mean for a binomial distribution with 10 trials and a success probability of 0.5
mean_value = ds.mean(10, 0.5)

# Calculate the standard deviation for a binomial distribution with 10 trials and a success probability of 0.5
std_dev = ds.standard_deviation(10, 0.5)
``` -->

### Function Descriptions

1.`validate_parameters(n, p)`

Validates the parameters of a binomial distribution.

    Input: 
            n (int) - The number of trials; p (float) - The probability of success.
    Output: 
            None
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

2.`mean(n, p)`

Calculates the mean of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The mean of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

3.`variance(n, p)`

Calculates the variance of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The variance of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

4.`standard_deviation(n, p)`

Calculates the standard deviation of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The standard deviation of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

5.`mode(n, p)`

Calculates the mode of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The mode of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

6.`skewness(n, p)`

Calculates the skewness of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The skewness of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

7.`kurtosis(n, p)`

Calculates the kurtosis of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The kurtosis of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

8.`entropy(n, p)`

Calculates the entropy of a binomial distribution.

    Input: 
            n (int) - The number of trials
            p (float) - The probability of success.
    Output: 
            (float) - The entropy of the binomial distribution.
    Raises: 
            ValueError if the input parameters are not valid for a binomial distribution.

### Example Usage

```python
import descriptive_statistics as ds

num_trials = 10
probability_success = 0.5

# Mean
binomial_mean = ds.mean(num_trials, probability_success)
print(f"The mean of the binomial distribution is {binomial_mean:.2f}")

# Standard Deviation
binomial_std = ds.standard_deviation(num_trials, probability_success)
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

# Parameter estimation module

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
    Output: 
        (tuple) - A tuple containing the estimated number of trials (int) and the estimated probability of success (float).
    Raises: 
        ValueError - If the sample data is empty or if the sample variance is zero.
        
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
        
        
### Example usage

``` python 
import parameter_estimation as be

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

print("Confidence intervals:")

ci_normal = be.confidence_interval_normal_approximation(sample_data)
print("Normal approximation:", ci_normal)

ci_clopper_pearson = be.confidence_interval_clopper_pearson(sample_data)
print("Clopper-Pearson:", ci_clopper_pearson)

ci_agresti_coull = be.confidence_interval_agresti_coull(sample_data)
print("Agresti-Coull:", ci_agresti_coull)
```

# Hypothesis testing module

This Python module provides functions to perform various statistical tests and calculations related to binomial proportions. It includes the proportion z-test, continuity corrected proportion z test, power analysis, Fisher's exact test, chi-square test, G-test for goodness-of-fit, confidence interval calculation, and Cohen's h effect size calculation.

1. `proportion_z_test(successes1, trials1, successes2, trials2, alternative='two-sided')`: This function performs a proportion z-test to compare two binomial proportions. It calculates the p-value for the comparison.
2. `power_analysis_binomial_proportions(p1, p2, alpha=0.05, power=0.8, alternative='two-sided', ratio=1)`: This function performs a power analysis for a proportion z-test comparing two binomial proportions to determine the required sample size.
3. `fishers_exact_test(success1, total1, success2, total2, alternative='two-sided')`: This function performs Fisher's exact test for equality of two binomial proportions. It calculates the p-value for the test.
4. `chi_square_test(binomial_data, expected_proportions=None)`: This function performs a chi-square test for the equality of multiple binomial proportions. It calculates the p-value for the test.
5. `g_test_goodness_of_fit(binomial_data, expected_proportions=None)`: This function performs a G-test for goodness-of-fit for binomial data. It calculates the p-value for the test.
6. `proportion_confidence_interval(success, trials, alpha=0.05)`: Calculates the confidence interval for a binomial proportion.
7. `cohen_h_effect_size(p1, p2)`: Calculates Cohen's h effect size for proportions.
8. `continuity_corrected_proportion_z_test(successes1, trials1, successes2, trials2, alternative='two-sided')`: Performs a continuity-corrected proportion z-test to compare two binomial proportions.

### Function Descriptions

1. `proportion_z_test(successes1, trials1, successes2, trials2, alternative='two-sided')`

Performs a proportion z-test to compare two binomial proportions.

    Input:
            successes1 (int): The number of successes in group 1
            trials1 (int): The total number of trials in group 1
            successes2 (int): The number of successes in group 2
            trials2 (int): The total number of trials in group 2
            alternative (str, optional): The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided') 
    Output:
            p_value (float): The p-value of the test
    Raises:
            ValueError: If the input values for successes and trials are not integers, if trials1 or trials2 are 0, or if the alternative hypothesis is invalid
            
2. `power_analysis_binomial_proportions`

Performs a power analysis for a proportion z-test comparing two binomial proportions to determine the required sample size.

    Input:
            p1 (float): The true proportion in group 1
            p2 (float): The true proportion in group 2
            alpha (float, optional): The desired significance level (default is 0.05)
            power (float, optional): The desired statistical power (default is 0.8)
                                     alternative (str, optional): The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')
            ratio (float, optional): The ratio of sample sizes between group 2 and group 1 (default is 1)  
    Output:
            sample_size1 (int): The required sample size for group 1
    Raises:
            ValueError: If the input values for p1, p2, alpha, power, and ratio are not numbers, or if p1, p2, alpha, and power are not between 0 and 1 (inclusive)    
            
3. `fishers_exact_test`

Performs Fisher's exact test for equality of two binomial proportions.

    Input:
            success1 (int): The number of successes in group 1
            total1 (int): The total number of trials in group 1
            success2 (int): The number of successes in group 2
            total2 (int): The total number of trials in group 2
            alternative (str, optional): The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')                                 
    Output:
            p_value (float): The p-value for the test
    Raises: 
            ValueError: If the input values for success1, total1, success2, and total2 are not integers, if total1 or total2 are negative, or if the alternative hypothesis is invalid.
            
4. `chi_square_test`

Performs a chi-square test for the equality of multiple binomial proportions.           

    Input:
            binomial_data (list): A list of tuples containing the number of successes and total trials for each group
            expected_proportions (list, optional): A list of expected proportions for each group. If not provided, the test will assume equal proportions.                                           
    Output:
            p_value (float): The p-value for the test
    Raises:
            ValueError: If binomial_data or expected_proportions are invalid, or if their lengths do not match

5. `g_test_goodness_of_fit`

Performs a G-test for goodness-of-fit for binomial data.

    Input:
            binomial_data (list): A list of tuples containing the number of successes and total trials for each group
            expected_proportions (list, optional): A list of expected proportions for each group. If not provided, the test will assume equal proportions.                                              
    Output:
            p_value (float): The p-value for the test
    Raises:
            ValueError: If binomial_data or expected_proportions are invalid, or if their lengths do not match

6. `proportion_confidence_interval`

Calculates the confidence interval for a binomial proportion.

    Input:
            success (int): The number of successes
            trials (int): The total number of trials
            alpha (float, optional): The desired significance level (default is 0.05)
    Output:
            confidence_interval (tuple): A tuple containing the lower and upper bounds of the confidence interval
    Raises:
            ValueError: If success or trials are not integers, or if alpha is not between 0 and 1 (inclusive)

7. `cohen_h_effect_size`

Calculates Cohen's h effect size for proportions.

    Input:
            p1 (float): The proportion for group 1
            p2 (float): The proportion for group 2
    Output:
            h (float): Cohen's h effect size
    Raises:
            ValueError: If p1 or p2 are not numbers (integers or floats)
            
8. `continuity_corrected_proportion_z_test`

Performs a continuity-corrected proportion z-test to compare two binomial proportions.

    Input:
            successes1 (int): The number of successes in group 1
            trials1 (int): The total number of trials in group 1
            successes2 (int): The number of successes in group 2
            trials2 (int): The total number of trials in group 2
            alternative (str, optional): The alternative hypothesis, 'two-sided', 'greater', or 'less' (default is 'two-sided')                                              
    Output:
            p_value (float): The p-value of the test
    Raises:
            ValueError: If the input values for successes and trials are not integers, or if the alternative hypothesis is invalid
            
### Usage

To use the functions provided in this module, simply import the module and call the desired function with the appropriate parameters:
```python
import hypothesis_testing as ht

#proportion_z_test
successes1 = 80
trials1 = 100
successes2 = 70
trials2 = 100
alternative = 'two-sided'

p_value = ht.proportion_z_test(successes1, trials1, successes2, trials2, alternative)
print("Proportion Z-Test p-value:", p_value)


# power_analysis_binomial_proportions
p1 = 0.8
p2 = 0.7
alpha = 0.05
power = 0.8
alternative = 'two-sided'
ratio = 1

sample_size1 = ht.power_analysis_binomial_proportions(p1, p2, alpha, power, alternative, ratio)
print("Required sample size for group 1:", sample_size1)


# fishers_exact_test
success1 = 80
total1 = 100
success2 = 70
total2 = 100
alternative = 'two-sided'

p_value = ht.fishers_exact_test(success1, total1, success2, total2, alternative)
print("Fisher's Exact Test p-value:", p_value)


# chi_square_test
binomial_data = [(80, 100), (70, 100), (90, 100)]
expected_proportions = [1/3, 1/3, 1/3]

p_value = ht.chi_square_test(binomial_data, expected_proportions)
print("Chi-Square Test p-value:", p_value)


# g_test_goodness_of_fit
binomial_data = [(80, 100), (70, 100), (90, 100)]
expected_proportions = [1/3, 1/3, 1/3]

p_value = ht.g_test_goodness_of_fit(binomial_data, expected_proportions)
print("G-Test Goodness-of-Fit p-value:", p_value)


# proportion_confidence_interval
success = 80
trials = 100
alpha = 0.05

lower_bound, upper_bound = ht.proportion_confidence_interval(success, trials, alpha)
print("Proportion Confidence Interval:", (lower_bound, upper_bound))


# cohen_h_effect_size
p1 = 0.8
p2 = 0.7

h = ht.cohen_h_effect_size(p1, p2)
print("Cohen's h Effect Size:", h)


# continuity_corrected_proportion_z_test
successes1 = 50
trials1 = 100
successes2 = 60
trials2 = 120
alternative = 'two-sided'

p_value = ht.continuity_corrected_proportion_z_test(successes1, trials1, successes2, trials2, alternative)
print("The p-value is:", p_value)


```           

# Binomial Simulation Module            

This Python module provides a class for simulating and analyzing binomial experiments. The class includes methods for running the simulation, plotting histograms and success probability evolution, performing various hypothesis tests (proportion z-test, Fisher's exact test, chi-square test), and cross-validation of hypothesis testing.

Class: `BinomialSimulation`

**Attributes:**
1. `n_trials (int)`: The number of trials in each experiment.
2. `p_success (float)`: The probability of success in each trial.
3. `n_experiments (int)`: The number of experiments to simulate.
4. `results (ndarray or None)`: An array containing the results of the simulations, or None if the simulation has not been run.

**Methods:**
1. `__init__(self, n_trials, p_success, n_experiments)`: Initializes the BinomialSimulation object with the given parameters.
2. `run_simulation(self)`: Runs the binomial simulation.
3. `plot_histogram(self, bins=None)`: Plots a histogram of the simulation results.
4. `plot_success_probability_evolution(self, window_size=10)`: Plots the evolution of success probabilities.
5. `perform_hypothesis_testing(self, test_type, **kwargs)`: Performs hypothesis testing on the simulated results.
6. `calculate_metrics(self, test_data)`: Calculates various metrics for the binomial experiment.
7. `cross_validate_hypothesis_testing(self, test_type, n_folds=5, **kwargs)`: Performs cross-validation of hypothesis testing on the simulated results.
8. `get_results(self)`: Returns the simulation results.

### Function Descriptions

1. `__init__(self, n_trials, p_success, n_experiments)`

Initializes the BinomialSimulation object with the given parameters.

    Input:
            n_trials (int): The number of trials per experiment
            p_success (float): The probability of success per trial
            n_experiments (int): The number of experiments to simulate
    Output:
            None

2. `run_simulation(self)`

Runs the binomial simulation.

    Input:
            None
    Output:
            None
            
3. `plot_histogram(self, bins=None)`

Plots a histogram of the simulation results.
           
    Input:
            bins (int or sequence of scalars, optional): If bins is an int, it defines the number of equal-width
            bins in the given range (10, by default). If bins is a sequence, it defines the bin edges, including the
            left edge of the first bin and the right edge of the last bin; in this case, bins may be unequally
            spaced
    Output:
            None

4. `plot_success_probability_evolution(self, window_size=10)`

Plots the evolution of success probabilities in the simulated experiments.

    Input:
            window_size (int, optional): The size of the sliding window to use for calculating the moving average
        (10 by default)
    Output:
            None
            
 5. `perform_hypothesis_testing(self, test_type, **kwargs)`

Performs hypothesis testing on the simulated results using the specified test type and input values provided in the kwargs. The input values required depend on the test type being used, and should be provided in the kwargs dictionary.   

    Input:
            test_type (str): The type of hypothesis test to perform ('proportion_z_test', 'fishers_exact_test', or 'chi_square_test')
            **kwargs: Additional keyword arguments to pass to the hypothesis test function
    Output:
            p_value (float): The p-value resulting from the hypothesis test


6. `calculate_metrics(self, test_data)`

Calculates various metrics for the binomial experiment.

    Input:
            test_data (list): A list of results for the test data
    Output:
            dict: A dictionary containing the mean, median, and standard deviation
            
7. `cross_validate_hypothesis_testing(self, test_type, n_folds=5, **kwargs)`

Performs cross-validation of hypothesis testing on the simulated results using the specified test type and input values provided in the kwargs. The input values required depend on the test type being used, and should be provided in the kwargs dictionary.           

    Input:
            test_type (str): The type of hypothesis test to perform ('proportion_z_test', 'fishers_exact_test', or         'chi_square_test')
            n_folds (int, optional): The number of folds to use for cross-validation (5 default)
            **kwargs: Additional keyword arguments to pass to the cross validate hypothesis test function
    Output:
            dict: A dictionary containing the average performance metrics across all folds
            
 8. `get_results(self)`           

Returns the results of the simulation.

    Input:
            None
    Output:
            ndarray: An array containing the results of the simulations

### Example Usage

``` python
import numpy as np
from scipy import stats

# Initialize the BinomialSimulation object
n_trials = 10
p_success = 0.5
n_experiments = 1000
binomial_simulation = BinomialSimulation(n_trials, p_success, n_experiments)

# Run the simulation
binomial_simulation.run_simulation()

# Plot a histogram of the results
binomial_simulation.plot_histogram()

# Plot the evolution of success probabilities
binomial_simulation.plot_success_probability_evolution()

# Perform hypothesis testing using the proportion_z_test
p_value_proportion_z_test = binomial_simulation.perform_hypothesis_testing(
    test_type='proportion_z_test',
    successes1=40,
    trials1=100,
    successes2=30,
    trials2=100
)
print("Proportion z-test p-value:", p_value_proportion_z_test)

# Perform hypothesis testing using the chi_square_test
example_binomial_data = [(20, 30), (25, 35), (18, 22), (30, 20)]
p_value_chi_square_test = binomial_simulation.perform_hypothesis_testing(
    test_type='chi_square_test',
    binomial_data=example_binomial_data
)
print("Chi-square test p-value:", p_value_chi_square_test)

# Cross-validate hypothesis testing using the proportion_z_test
avg_metrics = binomial_simulation.cross_validate_hypothesis_testing(
    test_type='proportion_z_test',
    n_folds=5,
    successes1=40,
    trials1=100,
    successes2=30,
    trials2=100
)
print("Cross-validation average metrics:", avg_metrics)

```
