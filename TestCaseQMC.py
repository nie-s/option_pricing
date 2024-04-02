import unittest  
import numpy as np  
from QMonteCarloKIKOPut import QMonteCarloKIKOPut  
import csv
  

# Fix the parameters  
r = 0.06  
R = 5
m = 100000  # Number of paths
T = 1.0  
n = 10
sigma0 = 0.1


# Set the random seed for reproducibility  
np.random.seed(42)  

class TestQMC(unittest.TestCase):  
    def __init__(self, *args, **kwargs):  
        super(TestQMC, self).__init__(*args, **kwargs)  
        self.results_file = 'KIKO_options_results.csv'  
        self.header_written = False

    def write_to_csv(self, row):  
        with open(self.results_file, mode='a', newline='') as csv_file:  
            writer = csv.writer(csv_file)  
            if not self.header_written:  
                # 写入表头  
                header = ['s0', 'K', 'L', 'U', 'R', 'r', 'sigma0', 'T', 'n', 'm', 'option_price', 'delta']  
                writer.writerow(header)  
                self.header_written = True  
            # 写入结果行  
            writer.writerow(row)    
  
    def test_qmc(self):  
        # Test put options
        s0 = [9.5, 10, 10.5, 9.8, 10.2] 
        K = [9, 9, 9, 9, 9]
        L = [9.3, 9.6, 10.1, 9.5, 9.8]
        U = [10.2, 10.4, 10.9, 11, 11]
         
        
        for s0_i, K_i, L_i, U_i in zip(s0, K, L, U):  
            qmc_test = QMonteCarloKIKOPut(s0_i, K_i, L_i, U_i, R, r, sigma0, T, m, n)  
        
            option_price,delta = qmc_test.calculate_price_and_delta()   
            ##self.assertGreaterEqual(option_price, 0, f"QMC put option price should be non-negative for s0={s0_i}, K={K_i}, L={L_i}, U={U_i}")
            ##self.assertGreaterEqual(delta, 0, f"QMC put option delta should be non-negative for s0={s0_i}, K={K_i}, L={L_i}, U={U_i}")  
            kikoPut = [s0_i, K_i, L_i, U_i, R, r, sigma0, T, n, m, option_price, delta]  
            self.write_to_csv(kikoPut)
      
if __name__ == '__main__':  
    unittest.main()
