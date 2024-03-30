import unittest  
import numpy as np  
from BionomalTreeAmerican import BionomalTreeAmerican  
  
# Fix the parameters   
sigma = 0.4
r = 0.1
n = 200
  
# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAmericaOptions(unittest.TestCase):  
      
    def test_put_america(self):  
        # Test put options 
        s0 = [50, 50, 50]  
        K = [40, 50, 70]  
        T = [2, 2, 2]  
        
        for s0_i, K_i, T_i in zip(s0, K, T):  
            america_price = BionomalTreeAmerican(s0_i, sigma, r, T_i, K_i, n, 'put')  

            C = america_price.american_fast_tree()  
            self.assertGreaterEqual(C, 0, f"Bionomal Tree American put option price should be non-negative for s0={s0_i}, K={K_i}, T={T_i}")
            
          
    def test_call_america(self):  
        # Test put options 
        s0 = [50, 50, 50]  
        K = [40, 50, 70]  
        T = [2, 2, 2]  
        
        for s0_j, K_j, T_j in zip(s0, K, T):  
            america_price = BionomalTreeAmerican(s0_j, sigma, r, T_j, K_j, n, 'call')  
        
            C = america_price.american_fast_tree()  
            self.assertGreaterEqual(C, 0, f"Bionomal Tree American call option price should be non-negative for s0={s0_j}, K={K_j}, T={T_j}")
                
            
if __name__ == '__main__':  
    unittest.main()
