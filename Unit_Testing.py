import Variance_Testing as vt
import descriptive_statistics as ds 
import Probability
import unittest

def test_variance():
    
    variance_test = []
    
    odds = vt.odds_ratio(15, 50, 30, 100)
    risk = vt.relative_risk(10, 20, 40, 30)
    average = vt.mean([6, 4, 3, 7])
    st_dev = vt.standard_deviation([5, 5, 6, 6])
    binomial = vt.binomial_variance(20, 0.5)
    
    variance_test.append(odds)
    variance_test.append(risk)
    variance_test.append(average)
    variance_test.append(st_dev)
    variance_test.append(binomial)
    
    assert vt.odds_ratio(15, 50, 30, 100) == 1
    print('variance = ', variance_test)
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
    
    print('descriptive stats = ', stats_test)
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
    
    print('probability = ', probability_test)
    return probability_test

class TestBinomialDistribution(unittest.TestCase):
    
    def assert_variance(self):
        variance_test = test_variance()
        self.assertEquals(variance_test[0], 1.0)
        self.assertEquals(variance_test[1], 0.5)
        self.assertEquals(variance_test[2], 5.0)
        self.assertEquals(variance_test[3], 0.5)
        self.assertEquals(variance_test[4], 5.0)
    
def main():
    
    test_variance()
    test_descriptive_stats()
    test_probability()
    unittest.main(verbosity = 3)
    
if __name__ == "__main__":
    main()
