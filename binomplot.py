#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import matplotlib.pyplot as plt
from descriptive_statistics import standard_deviation
from Probability import ( pmf, cdf)

def plot_pmf(n,p):
    '''The plot_probability_mass_function() method creates a plot of the probability mass function 
    (PMF) of the binomial distribution using the plot() function of Matplotlib. The x_values are the
    possible values of k ranging from 0 to n, and the y_values are the corresponding probabilities
    calculated using the calculate_probability() method of the Binomial class. The title(), xlabel(), 
    and ylabel() functions are used to add labels to the plot. Finally, the show() function is called 
    to display the plot.'''
    x_values = list(range(n + 1))
    y_values = [pmf(k,n,p) for k in x_values]
    plt.plot(x_values, y_values)
    plt.title('Binomial PMF')
    plt.xlabel('k')
    plt.ylabel('Probability')
    plt.show()
    return

def plot_cdf(n,p):
    '''The CDF of the binomial distribution can be plotted using the plot() function of Matplotlib.
     The x_values are the possible values of k ranging from 0 to n, and the y_values are the corresponding 
    cumulative probabilities calculated using the calculate_cumulative_probability() method of the Binomial 
    class. Here's an example code:'''
    x_values = list(range(n + 1))
    y_values = [cdf(k,n,p) for k in x_values]
    plt.plot(x_values, y_values)
    plt.title('Binomial CDF')
    plt.xlabel('k')
    plt.ylabel('Cumulative Probability')
    plt.show()
    return

def plot_cdfbarchart(n,p):
    '''method to plot the CDF of a binomial distribution'''
    x_values = list(range(n + 1))
    y_values = [cdf(k,n,p) for k in x_values]
    plt.bar(x_values, y_values)
    plt.title('Binomial PMF')
    plt.xlabel('k')
    plt.ylabel('Probability')
    plt.show()
    return
   
def plot_pmfbarchart(n,p):
    '''method to plot the CDF of a binomial distribution'''
    x_values = list(range(n + 1))
    y_values = [pmf(k,n,p) for k in x_values]
    plt.bar(x_values, y_values)
    plt.title('Binomial PMF')
    plt.xlabel('k')
    plt.ylabel('Probability')
    plt.show()
    return 


def plot_pmflinechart(n,p):
    '''line plot of the probability mass function with error
    bars using the errorbar() function of Matplotlib. Here's an example code:'''
    x_values = list(range(n + 1))
    y_values = [pmf(k,n,p) for k in x_values]
    std_dev = standard_deviation(n,p)
    error_values = [std_dev * math.sqrt(y * (1 - y) / n) for y in y_values]
    plt.errorbar(x_values, y_values, yerr=error_values, fmt='o-', capsize=5)
    plt.title('Binomial PMF')
    plt.xlabel('k')
    plt.ylabel('Probability')
    plt.show()
    return
    
def plot_cdflinechart(n,p):
    '''line plot of the probability mass function with error
    bars using the errorbar() function of Matplotlib. Here's an example code:'''
    x_values = list(range(n + 1))
    y_values = [cdf(k,n,p) for k in x_values]
    std_dev = standard_deviation(n,p)
    error_values = [std_dev * math.sqrt(y * (1 - y) / n) for y in y_values]
    plt.errorbar(x_values, y_values, yerr=error_values, fmt='o-', capsize=5)
    plt.title('Binomial PMF')
    plt.xlabel('k')
    plt.ylabel('Probability')
    plt.show()
    return


# In[ ]:




