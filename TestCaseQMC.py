import unittest  
import numpy as np  
from QMonteCarloKIKOPut import QMonteCarloKIKOPut  
  
# Fix the parameters  
r = 0.06  
T = 1.0  
s0 = 10
m = 100000  # Number of paths 
K = 9 
sigma0 = 0.1
n = 10

# Set the random seed for reproducibility  
np.random.seed(42)  

class TestQMC(unittest.TestCase):  
      
    def test_qmc(self):  
        # Test put options 
        L = [7, 8, 9]
        U = [11, 12, 13]
        R = [5, 6, 7]
         
        
        for L_i, U_i, R_i in zip(L, U, R):  
            qmc_test = QMonteCarloKIKOPut(s0, K, L_i, U_i, R_i, r, sigma0, T, m, n)  
        
            option_price,delta = qmc_test.calculate_price_and_delta()   
            self.assertGreaterEqual(option_price, 0, f"QMC put option price should be non-negative for L={L_i}, U={U_i}, R={R_i}")
            self.assertGreaterEqual(delta, 0, f"QMC put option delta should be non-negative for L={L_i}, U={U_i}, R={R_i}")  
 
      
    
            
if __name__ == '__main__':  
    unittest.main()
