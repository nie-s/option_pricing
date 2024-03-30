import unittest  
import numpy as np  
from MonteCarloAsianVC import MonteCarloAsianVC  
  
# Fix the parameters  
r = 0.05  
T = 3  
s0 = 100  
m = 100000  # Number of paths  
  
# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAsianOptions(unittest.TestCase):  
      
    def test_put_options(self):  
        # Test put options 
        sigma = [0.3, 0.3, 0.4]  
        K = [100, 100, 100]  
        n = [50, 100, 50]  
        
        for sigma_i, K_i, n_i in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(s0, sigma_i, r, T, K_i, m, n_i, 'put', False)  
        
            mc_value_without_cv, lower_bound_without_cv, upper_bound_without_cv = asian_vc.value()   
            self.assertGreaterEqual(mc_value_without_cv, 0, f"Put option MC value without control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")
            self.assertGreaterEqual(lower_bound_without_cv, 0, f"Put option lower_bound value without control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")  
            self.assertGreaterEqual(upper_bound_without_cv, 0, f"Put option upper_bound value without control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}") 
          
        for sigma_i, K_i, n_i in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(s0, sigma_i, r, T, K_i, m, n_i, 'put', True)  
        
            value_with_control_variate, lower_bound_CV, upper_bound_CV = asian_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Put option MC value with control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")
            self.assertGreaterEqual(lower_bound_CV, 0, f"Put option lower_bound value with control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Put option upper_bound_CV value with control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")
      
    def test_call_options(self):  
        # Test call options  
        sigma = [0.3, 0.3, 0.4]  
        K = [100, 100, 100]  
        n = [50, 100, 50]  
        
        for sigma_j, K_j, n_j in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(s0, sigma_j, r, T, K_j, m, n_j, 'call', False)  
            
            mc_value_without_cv, lower_bound_without_cv, upper_bound_without_cv = asian_vc.value()   
            self.assertGreaterEqual(mc_value_without_cv, 0, f"Call option MC value without control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")
            self.assertGreaterEqual(lower_bound_without_cv, 0, f"Call option lower_bound value without control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")  
            self.assertGreaterEqual(upper_bound_without_cv, 0, f"Call option upper_bound value without control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}") 

        for sigma_i, K_i, n_i in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(s0, sigma_i, r, T, K_i, m, n_i, 'call', True) 
 
            value_with_control_variate, lower_bound_CV, upper_bound_CV = asian_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Call option price with control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}") 
            self.assertGreaterEqual(lower_bound_CV, 0, f"Call option lower_bound with control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Call option upper_bound with control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")   
              
            
if __name__ == '__main__':  
    unittest.main()
