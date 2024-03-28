import unittest  
import numpy as np  
from MonteCarloAsianVC import MonteCarloAsianVC  
  
# Fix the parameters  
r = 0.05  
T = 3  
S0 = 100  
m = 100000  # Number of paths  
  
# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAsianOptions(unittest.TestCase):  
      
    def test_put_options(self):  
        # Test put options 
        sigma = [0.3, 0.3, 0.4]  
        K = [100] * 3  
        n = [50, 100] * 2 + [50]  
          
        for sigma_i, K_i, n_i in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(S0, sigma_i, r, T, K_i, m, n_i, 'put')  
              
            # 不使用控制变量  
            mc_value_without_cv, lower_bound_without_cv, upper_bound_without_cv = asian_vc.value()   
            self.assertGreaterEqual(mc_value_without_cv, 0, f"Put option MC value without control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")
            self.assertGreaterEqual(lower_bound_without_cv, 0, f"Put option lower_bound value without control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")  
            self.assertGreaterEqual(upper_bound_without_cv, 0, f"Put option upper_bound value without control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")    
              
            # 使用控制变量  
            value_with_control_variate, lower_bound_CV, upper_bound_CV = asian_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Put option MC value with control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")
            self.assertGreaterEqual(lower_bound_CV, 0, f"Put option lower_bound value with control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Put option upper_bound_CV value with control variate should be non-negative for sigma={sigma_i}, K={K_i}, n={n_i}")    
 
            # 可选：如果有预期的价格，可以进行更精确的断言  
            # self.assertAlmostEqual(asian_price_without_cv, expected_price_without_cv, places=decimal_places)  
            # self.assertAlmostEqual(asian_price_with_cv, expected_price_with_cv, places=decimal_places)  
      
    def test_call_options(self):  
        # Test call options  
        sigma = [0.3, 0.3, 0.4]  
        K = [100] * 3  
        n = [50, 100] * 2 + [50]  
          
        for sigma_j, K_j, n_j in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(S0, sigma_j, r, T, K_j, m, n_j, 'call')  
              
            # 不使用控制变量  
            mc_value_without_cv, lower_bound_without_cv, upper_bound_without_cv = asian_vc.value()   
            self.assertGreaterEqual(mc_value_without_cv, 0, f"Call option MC value without control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")
            self.assertGreaterEqual(lower_bound_without_cv, 0, f"Call option lower_bound value without control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")  
            self.assertGreaterEqual(upper_bound_without_cv, 0, f"Call option upper_bound value without control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}") 
              
            # 使用控制变量  
            value_with_control_variate, lower_bound_CV, upper_bound_CV = asian_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Call option price with control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}") 
            self.assertGreaterEqual(lower_bound_CV, 0, f"Call option lower_bound with control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Call option upper_bound with control variate should be non-negative for sigma={sigma_j}, K={K_j}, n={n_j}")   
              
            # 可选：如果你有预期价格，可以进行更精确的断言  
            # self.assertAlmostEqual(asian_price_without_cv, expected_price_without_cv, places=decimal_places)  
            # self.assertAlmostEqual(asian_price_with_cv, expected_price_with_cv, places=decimal_places)  
  
if __name__ == '__main__':  
    unittest.main()
