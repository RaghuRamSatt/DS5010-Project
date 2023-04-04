# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 11:49:41 2023

@author: hasan
"""

import math

def odds_ratio(exposed_yes, not_exposed_yes, exposed_no, not_exposed_no):
    """
    Funtion
    --------
    odds of first group divided by odds of the second
    Used to determine the association between two variables 
    
    Parameters
    ----------
    exposed_yes: cases that were exposed and have the outcome 
    not_exposed_yes: cases that were not exposed and have the outcome
    exposed_no: cases that were exposed and do not have the outcome
    not_exposed_no: cases that were not exposed and do not have the outcome

    Returns
    -------
    odds - odds of an event occuring 
    """
    
    odds_exposed = exposed_yes/not_exposed_yes
    odds_not_exposed = exposed_no/not_exposed_no
    
    odds = odds_exposed/odds_not_exposed
    
    return odds

def relative_risk(exposed_yes, not_exposed_yes, exposed_no, not_exposed_no):
    """
    Function
    --------
    caluclates the risk of an outcome occuring between a case group and control
    used when comparing the likelyhood of an outcome occuring

    Parameters
    ----------
    exposed_yes: cases that were exposed and have the outcome 
    not_exposed_yes: cases that were not exposed and have the outcome 
    exposed_no: cases that were exposed and do not have the outcome
    not_exposed_no: cases that were not exposed and do not have the outcome

    Returns
    -------
    risk : ratio of the probability of an outcome occuring 

    """
    
    risk_exposed = exposed_yes / (exposed_yes + exposed_no)
    risk_not_exposed = not_exposed_yes / (not_exposed_yes + not_exposed_no)
    
    risk = risk_exposed / risk_not_exposed
    
    return risk 

def mean(data_lst):
    """
    Function
    ------
    Calculates the mean of a given data set

    Parameters
    ----------
    data_lst: list of data points 

    Returns
    -------
    Mean as it may be used in further testing
    """
    
    total = sum(data_lst)
    mean = total / len(data_lst)
    
    return mean

def standard_deviation(data_lst):
    """
    Method
    ------
    Calculates standard deviation of a given data set
    
    Parameters
    ----------
    data_lst: list of data points
    
    Returns
    -------
    Standard deviation to be used in further testing 
    """
    
    average = mean(data_lst)
    
    square_distance = []
    for i in range(len(data_lst)):
        distance = abs(data_lst[i] - average)
        square_distance.append(distance ** 2)
        
    distance_by_data = sum(square_distance) / len(data_lst)
    standard_deviation = math.sqrt(distance_by_data)
    
    return standard_deviation

def t_test(mean1, mean2, stdev1, stdev2, count1, count2, alpha):
    """
    Function
    --------
    compares the mean between two groups 
    
    Parameters
    ----------
    mean_1: mean of first set
    mean_2: mean of second set
    stdev_1: standard deviation of first set
    stdev2_: standard deviation of second set
    count1_: number of elements of first set
    count2_: number of elements of second set

    Returns
    -------
    State of the null hypothesis 
    """
    
    mean_difference = abs(mean1 - mean2)
    stdev_count_1 = (stdev1 ** 2) / count1
    stdev_count_2 = (stdev2 ** 2) / count2
    root = math.sqrt(stdev_count_1 + stdev_count_2)
    
    t_value = mean_difference / root
    
    degrees_of_freedom = (count1 + count2) - 2
    
    critical_value = scipy.stats.t.ppf(alpha, degrees_of_freedom)
    
    if t_value < critical_value:
        return "Reject null hypothesis"
    else:
        return "Fail to reject null hypothesis"


def binomial_variance(number_trials, probability_success):
    """
    Function
    --------
    calculates the variance of the binmial distribution
    
    Parameters
    ----------
    number_trials: number of independent trials
    probability_success: probability of success of a trial 
    
    Returns
    -------
    variance in terms of the expected amount of success 
    
    """
    
    variance = (number_trials * probability_success) * (1 - probability_success)
    
    return variance

def z_test(sample_size, null_hypothesized_value, observed_proportion, alpha):
    """
    Function

    Parameters
    ----------
    sample_size : total number of data points in a set
    null_hypothesized_value : hypothesized value of the population proportion
    observed_proportion : sample population
    alpha : level of significance 

    Returns
    -------
    State of the null hypothesis 
    """
    
    numerator = observed_proportion - null_hypothesized_value 
    
    hypothesized_value = null_hypothesized_value * (1 - null_hypothesized_value)  
                          
    denominator = math.sqrt(hypothesized_value / sample_size)
    
    z_score = numerator / denominator
    
    critical_value = scipy.stats.norm.ppf(alpha)
    
    if z_score < critical_value:
        return "Reject null hypothesis"
    else:
        return "Fail to reject null hypothesis"


