import unittest  
import numpy as np  
from MonteCarloAsianVC import MonteCarloAsianVC  
import csv
  
# Fix the parameters  
r = 0.05  
T = 3  
s0 = 100  
m = 100000  # Number of paths  
  
# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAsianOptions(unittest.TestCase):  
    def __init__(self, *args, **kwargs):  
        super(TestMonteCarloAsianOptions, self).__init__(*args, **kwargs)  
        self.results_file = 'asian_options_results.csv'  
        self.header_written = False


    def write_to_csv(self, row):  
        with open(self.results_file, mode='a', newline='') as csv_file:  
            writer = csv.writer(csv_file)  
            if not self.header_written:  
                # 写入表头  
                header = ['s0','K', 'T', 'sigma', 'r', 'n', 'with_cv', 'option_type', 'value', 'lower_bound', 'upper_bound']  
                writer.writerow(header)  
                self.header_written = True  
            # 写入结果行  
            writer.writerow(row)  


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
            row_without_cv = [s0, K_i, T, sigma_i, r, n_i, False, 'put', mc_value_without_cv, lower_bound_without_cv, upper_bound_without_cv]  
            self.write_to_csv(row_without_cv)

        for sigma_p, K_p, n_p in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(s0, sigma_p, r, T, K_p, m, n_p, 'put', True)  
        
            value_with_control_variate, lower_bound_CV, upper_bound_CV = asian_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Put option MC value with control variate should be non-negative for sigma={sigma_p}, K={K_p}, n={n_p}")
            self.assertGreaterEqual(lower_bound_CV, 0, f"Put option lower_bound value with control variate should be non-negative for sigma={sigma_p}, K={K_p}, n={n_p}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Put option upper_bound_CV value with control variate should be non-negative for sigma={sigma_p}, K={K_p}, n={n_p}")
            row_with_cv = [s0, K_p, T, sigma_p, r, n_p, True, 'put', value_with_control_variate, lower_bound_CV, upper_bound_CV]  
            self.write_to_csv(row_with_cv) 


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
            row_without_cv_call = [s0, K_j, T, sigma_j, r, n_j, False, 'call', mc_value_without_cv, lower_bound_without_cv, upper_bound_without_cv]  
            self.write_to_csv(row_without_cv_call)


        for sigma_q, K_q, n_q in zip(sigma, K, n):  
            asian_vc = MonteCarloAsianVC(s0, sigma_q, r, T, K_q, m, n_q, 'call', True) 
 
            value_with_control_variate, lower_bound_CV, upper_bound_CV = asian_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Call option price with control variate should be non-negative for sigma={sigma_q}, K={K_q}, n={n_q}") 
            self.assertGreaterEqual(lower_bound_CV, 0, f"Call option lower_bound with control variate should be non-negative for sigma={sigma_q}, K={K_q}, n={n_q}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Call option upper_bound with control variate should be non-negative for sigma={sigma_q}, K={K_q}, n={n_q}")   
            row_with_cv_call = [s0, K_q, T, sigma_q, r, n_q, True, 'call', value_with_control_variate, lower_bound_CV, upper_bound_CV]  
            self.write_to_csv(row_with_cv_call)  
            
if __name__ == '__main__':  
    unittest.main()
