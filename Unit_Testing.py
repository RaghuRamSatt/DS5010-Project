import Variance_Testing as vt
import descriptive_statistics as ds 
import Probability
import hypothesis_testing as ht 
import parameter_estimation as pe
import random_sampling as rs 
import unittest

def test_variance_testing():
    
    variance_test = []
    
    odds = vt.odds_ratio(15, 50, 30, 100)
    risk = vt.relative_risk(10, 20, 40, 30)
    average = vt.mean([6, 4, 3, 7])
    st_dev = vt.standard_deviation([5, 5, 6, 6])
    binomial = vt.binomial_variance(20, 0.5)
    t_test = vt.t_test(9.59, 7.35, 19.31, 24.02, 13, 13, 0.5)
    z_test = vt.z_test(120, 0.26, 0.33, 0.05)
    
    variance_test.append(odds)
    variance_test.append(risk)
    variance_test.append(average)
    variance_test.append(st_dev)
    variance_test.append(binomial)
    variance_test.append(t_test)
    variance_test.append(z_test)
    
    return variance_test

def test_descriptive_stats():
    
    stats_test = []
    
    valid = ds.validate_parameters(10, 0.5)
    binomial_mean = ds.mean(10, 0.5)
    variance = ds.variance(10, 0.5)
    binomial_st_dev = ds.standard_deviation(10, 0.5)
    mode = ds.mode(10, 0.5)
    skew = ds.skewness(10, 0.5)
    kurtosis = ds.kurtosis(10, 0.5)
    entropy = ds.entropy(10, 0.5)
    
    stats_test.append(valid)
    stats_test.append(binomial_mean)
    stats_test.append(variance)
    stats_test.append(binomial_st_dev)
    stats_test.append(mode)
    stats_test.append(skew)
    stats_test.append(kurtosis)
    stats_test.append(entropy)
    
    return stats_test

def test_probability():
    
    probability_test = []
    
    valid_prob = Probability.validate_parameters(10, 0.5)
    fact = Probability.factorial(10)
    coefficient = Probability.binomial_coefficient(10, 5)
    pmf = Probability.pmf(5, 10, 0.5)
    cdf = Probability.cdf(10, 10, 0.5)
    
    probability_test.append(valid_prob)
    probability_test.append(fact)
    probability_test.append(coefficient)
    probability_test.append(pmf)
    probability_test.append(cdf)
    
    return probability_test

def test_hypothesis_testing():
    
    hypothesis_test = []
    
    z_test_two_sided = ht.proportion_z_test(5, 10, 2, 8)
    z_test_greater = ht.proportion_z_test(5, 10, 2, 8, 'greater')
    z_test_less = ht.proportion_z_test(5, 10, 2, 8, 'less')
    
    power_two_sided = ht.power_analysis_binomial_proportions(0.5, 0.25, 0.05, 0.2)
    power_greater = ht.power_analysis_binomial_proportions(0.5, 0.25, 0.05, 0.2, 'greater')
    power_less = ht.power_analysis_binomial_proportions(0.5, 0.25, 0.05, 0.2, 'less')
    
    fisher_two_sided = ht.fishers_exact_test(5, 10, 2, 8)
    fisher_greater = ht.fishers_exact_test(5, 10, 2, 8, 'greater')
    fisher_less = ht.fishers_exact_test(5, 10, 2, 8, 'less')
    
    hypothesis_test.append(z_test_two_sided)
    hypothesis_test.append(z_test_greater)
    hypothesis_test.append(z_test_less)
    hypothesis_test.append(power_two_sided)
    hypothesis_test.append(power_greater)
    hypothesis_test.append(power_less)
    hypothesis_test.append(fisher_two_sided)
    hypothesis_test.append(fisher_greater)
    hypothesis_test.append(fisher_less)
    
    return hypothesis_test
    
def test_parameter_estimation():
    
    param_test = []
    sample = [0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]
    
    parameters = pe.estimate_parameters(sample)
    log_like = pe.log_likelihood(0.5, sample)
    mle = pe.mle_estimate_parameters(sample)
    normal = pe.confidence_interval_normal_approximation(sample)
    clopper_pearson = pe.confidence_interval_clopper_pearson(sample)
    agresti_coull = pe.confidence_interval_agresti_coull(sample)
    
    param_test.append(parameters)
    param_test.append(log_like)
    param_test.append(mle)
    param_test.append(normal)
    param_test.append(clopper_pearson)
    param_test.append(agresti_coull)
    
    return param_test

def test_random_sampling():
    
    random_test = []
    
    bernoulli = rs.bernoulli_trial(1)
    binomial = rs.binomial_sample(1, 0)
    generate = rs.generate_binomial_samples(5, 10, 0.5, 500)
    
    random_test.append(bernoulli)
    random_test.append(binomial)
    random_test.append(generate)
    
    return random_test
    
class TestBinomialDistribution(unittest.TestCase):
    
    def test_variance(self):
        variance_test = test_variance_testing()
        self.assertEqual(variance_test[0], 1.0)
        self.assertEqual(variance_test[1], 0.5)
        self.assertEqual(variance_test[2], 5.0)
        self.assertEqual(variance_test[3], 0.5)
        self.assertEqual(variance_test[4], 5.0)
        self.assertEqual(variance_test[5], 'Fail to reject null hypothesis')
        self.assertEqual(variance_test[6], 'Fail to reject null hypothesis')
        
    def test_descriptive_stats(self):
        stats_test = test_descriptive_stats()
        self.assertEqual(stats_test[0], None)
        self.assertEqual(stats_test[1], 5.0)
        self.assertEqual(stats_test[2], 2.5)
        self.assertEqual(stats_test[3], 1.5811388300841898)
        self.assertEqual(stats_test[4], 5)
        self.assertEqual(stats_test[5], 0.0)
        self.assertEqual(stats_test[6], -0.2)
        self.assertEqual(stats_test[7], 11.0)
        
    def test_probability(self):
        prob_test = test_probability()
        self.assertEqual(prob_test[0], None)
        self.assertEqual(prob_test[1], 3628800)
        self.assertEqual(prob_test[2], 252)
        self.assertEqual(prob_test[3], 0.24609375)
        self.assertEqual(prob_test[4], 1.0)
        
    def test_hypothesis(self):
        hypo_test = test_hypothesis_testing()
        self.assertEqual(hypo_test[0], 0.27964153403730174)
        self.assertEqual(hypo_test[1], 0.13982076701865087)
        self.assertEqual(hypo_test[2], 0.8601792329813491)
        self.assertEqual(hypo_test[3], 10)
        self.assertEqual(hypo_test[4], 5)
        self.assertEqual(hypo_test[5], 5)
        self.assertEqual(hypo_test[6], 0.3665158371040724)
        self.assertEqual(hypo_test[7], 0.27828054298642535)
        self.assertEqual(hypo_test[8], 0.9434389140271493)
    
    def test_parameters(self):
        param_test = test_parameter_estimation()
        self.assertEqual(param_test[0], (1, 0.6153846153846154))
        self.assertEqual(param_test[1], -9.010913347279288)
        self.assertEqual(param_test[2], (1, 0.6153841996470607))
        self.assertEqual(param_test[3], (0.35092274920095196, 0.8798464815682789))
        self.assertEqual(param_test[4], (0.31577760291406304, 0.8614206611098394))
        self.assertEqual(param_test[5], (0.3540884254086416, 0.8240434117403896))
        
    def test_random_sampling(self):
        random_test = test_random_sampling()
        self.assertEqual(random_test[0], 1)
        self.assertEqual(random_test[1], 0)
        self.assertEqual(random_test[2], [3, 9, 6, 2, 2])
    
if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit = False, verbosity = 3)
