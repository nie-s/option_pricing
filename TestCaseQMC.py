import unittest  
import numpy as np  
from QMonteCarloKIKOPut import QMonteCarloKIKOPut  
  
# Fix the parameters  
r = 0.06  
T = 1.0  
n = 10
R = 5

m = 100000  # Number of paths 
sigma0 = 0.1


# Set the random seed for reproducibility  
np.random.seed(42)  

class TestQMC(unittest.TestCase):  
      
    def test_qmc(self):  
        # Test put options
        s0 = [10, 10, 10] 
        K = [9, 9, 9]
        L = [7, 8, 9]
        U = [11, 12, 13]
         
        
        for s0_i, K_i, L_i, U_i in zip(s0, K, L, U):  
            qmc_test = QMonteCarloKIKOPut(s0_i, K_i, L_i, U_i, R, r, sigma0, T, m, n)  
        
            option_price,delta = qmc_test.calculate_price_and_delta()   
            self.assertGreaterEqual(option_price, 0, f"QMC put option price should be non-negative for s0={s0_i}, K={K_i}, L={L_i}, U={U_i}")
            self.assertGreaterEqual(delta, 0, f"QMC put option delta should be non-negative for s0={s0_i}, K={K_i}, L={L_i}, U={U_i}")  
 
      
    
            
if __name__ == '__main__':  
    unittest.main()

