import unittest  
import numpy as np  
from MonteCarloBasket import MonteCarloBasketVC  
  
# Fix the parameters  
r = 0.05  
T = 3  
n = 100
m = 100000  # Number of paths  

# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAsianOptions(unittest.TestCase):  
      
    def test_put_basketoptions(self):  
        # Test put options 
        s1 = [100, 100, 100, 100, 100, 100]
        s2 = [100, 100, 100, 100, 100, 100]
        sigma1 = [0.3, 0.3, 0.1, 0.3, 0.3, 0.5]
        sigma2=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        rho =[0.5, 0.9, 0.5, 0.5, 0.5, 0.5]
        K =[100, 100, 100, 80, 120, 100] 
       
        for s1_i, s2_i, sigma1_i, sigma2_i, rho_i, K_i in zip(s1, s2, sigma1, sigma2, rho, K):  
            basket_vc = MonteCarloBasketVC(s1_i, s2_i, sigma1_i, sigma2_i, rho_i, r, T, K_i, n, m, 'put', False)   
        
            mc_value, lower_bound, upper_bound = basket_vc.value()   
            self.assertGreaterEqual(mc_value, 0, f"Put option MC value without control variate should be non-negative for s1={s1_i}, s2={s2_i}, sigma1={sigma1_i}, sigma2={sigma2_i}, rho={rho_i}, K={K_i}")
            self.assertGreaterEqual(lower_bound, 0, f"Put option lower_bound value without control variate should be non-negative for s1={s1_i}, s2={s2_i}, sigma1={sigma1_i}, sigma2={sigma2_i}, rho={rho_i}, K={K_i}")  
            self.assertGreaterEqual(upper_bound, 0, f"Put option upper_bound value without control variate should be non-negative for s1={s1_i}, s2={s2_i}, sigma1={sigma1_i}, sigma2={sigma2_i}, rho={rho_i}, K={K_i}") 
          
        for s1_i, s2_i, sigma1_i, sigma2_i, rho_i, K_i in zip(s1, s2, sigma1, sigma2, rho, K):    
            basket_vc = MonteCarloBasketVC(s1_i, s2_i, sigma1_i, sigma2_i, rho_i, r, T, K, n, m, 'put', True)  
        
            value_with_control_variate, lower_bound_CV, upper_bound_CV = basket_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Put option MC value with control variate should be non-negative for s1={s1_i}, s2={s2_i}, sigma1={sigma1_i}, sigma2={sigma2_i}, rho={rho_i}, K={K_i}")
            self.assertGreaterEqual(lower_bound_CV, 0, f"Put option lower_bound value with control variate should be non-negative for s1={s1_i}, s2={s2_i}, sigma1={sigma1_i}, sigma2={sigma2_i}, rho={rho_i}, K={K_i}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Put option upper_bound_CV value with control variate should be non-negative for s1={s1_i}, s2={s2_i}, sigma1={sigma1_i}, sigma2={sigma2_i}, rho={rho_i}, K={K_i}")
      
    def test_call_basketoptions(self):  
        # Test put options 
        s1 = [100, 100, 100, 100, 100, 100]
        s2 = [100, 100, 100, 100, 100, 100]
        sigma1 = [0.3, 0.3, 0.1, 0.3, 0.3, 0.5]
        sigma2=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        rho =[0.5, 0.9, 0.5, 0.5, 0.5, 0.5]
        K =[100,100,100,80,120,100]   
        
        for s1_j, s2_j, sigma1_j, sigma2_j, rho_j, K_j in zip(s1, s2, sigma1, sigma2, rho, K):  
            basket_vc = MonteCarloBasketVC(s1_j, s2_j, sigma1_j, sigma2_j, rho_j, r, T, K_j, n, m, 'call', False)    
            
            mc_value, lower_bound, upper_bound = basket_vc.value()    
            self.assertGreaterEqual(mc_value, 0, f"Call option MC value without control variate should be non-negative for s1={s1_j}, s2={s2_j}, sigma1={sigma1_j}, sigma2={sigma2_j}, rho={rho_j}, K={K_j}")
            self.assertGreaterEqual(lower_bound, 0, f"Call option lower_bound value without control variate should be non-negative for s1={s1_j}, s2={s2_j}, sigma1={sigma1_j}, sigma2={sigma2_j}, rho={rho_j}, K={K_j}")  
            self.assertGreaterEqual(upper_bound, 0, f"Call option upper_bound value without control variate should be non-negative for s1={s1_j}, s2={s2_j}, sigma1={sigma1_j}, sigma2={sigma2_j}, rho={rho_j}, K={K_j}") 

        for s1_j, s2_j, sigma1_j, sigma2_j, rho_j, K_j in zip(s1, s2, sigma1, sigma2, rho, K):  
            basket_vc = MonteCarloBasketVC(s1_j, s2_j, sigma1_j, sigma2_j, rho_j, r, T, K_j, n, m, 'call', True)
 
            value_with_control_variate, lower_bound_CV, upper_bound_CV = basket_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Call option price with control variate should be non-negative for s1={s1_j}, s2={s2_j}, sigma1={sigma1_j}, sigma2={sigma2_j}, rho={rho_j}, K={K_j}") 
            self.assertGreaterEqual(lower_bound_CV, 0, f"Call option lower_bound with control variate should be non-negative for s1={s1_j}, s2={s2_j}, sigma1={sigma1_j}, sigma2={sigma2_j}, rho={rho_j}, K={K_j}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Call option upper_bound with control variate should be non-negative for s1={s1_j}, s2={s2_j}, sigma1={sigma1_j}, sigma2={sigma2_j}, rho={rho_j}, K={K_j}")   
              
            
if __name__ == '__main__':  
    unittest.main()
