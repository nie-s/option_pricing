import unittest  
import numpy as np  
from BionomalTreeAmerican import BionomalTreeAmerican  
import csv
  
# Fix the parameters   
sigma = 0.4
r = 0.1
n = 200
  
# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAmericaOptions(unittest.TestCase):  
    def __init__(self, *args, **kwargs):  
        super(TestMonteCarloAmericaOptions, self).__init__(*args, **kwargs)  
        self.results_file = 'american_options_results.csv'  
        self.header_written = False

    def write_to_csv(self, row):  
        with open(self.results_file, mode='a', newline='') as csv_file:  
            writer = csv.writer(csv_file)  
            if not self.header_written:  
                # 写入表头  
                header = ['s0', 'K', 'T', 'sigma', 'r', 'n', 'option_type', 'Option Price']  
                writer.writerow(header)  
                self.header_written = True  
            # 写入结果行  
            writer.writerow(row)  


    def test_put_america(self):  
        # Test put options 
        s0 = [50, 50, 50]  
        K = [40, 50, 70]  
        T = [2, 2, 2]  
        
        
        for s0_i, K_i, T_i in zip(s0, K, T):  
            america_price = BionomalTreeAmerican(s0_i, sigma, r, T_i, K_i, n, 'put')  
            C = america_price.american_fast_tree()  
            self.assertGreaterEqual(C, 0, f"Bionomal Tree American put option price should be non-negative for s0={s0_i}, K={K_i}, T={T_i}")
            
            american_put = [s0_i, K_i, T_i, sigma, r, n, 'put', C]  
            self.write_to_csv(american_put)
         
  
          
    def test_call_america(self):  
        # Test put options 
        s0 = [50, 50, 50]  
        K = [40, 50, 70]  
        T = [2, 2, 2]   
        
        for s0_j, K_j, T_j in zip(s0, K, T):  
            america_price = BionomalTreeAmerican(s0_j, sigma, r, T_j, K_j, n, 'call')  
            C = america_price.american_fast_tree()  
            self.assertGreaterEqual(C, 0, f"Bionomal Tree American call option price should be non-negative for s0={s0_j}, K={K_j}, T={T_j}")
            american_call = [s0_j, K_j, T_j, sigma, r, n, 'call', C]  
            self.write_to_csv(american_call)
 

if __name__ == '__main__':  
    unittest.main()
