import unittest  
import numpy as np  
from MonteCarloBasket import MonteCarloBasketVC  
import csv
  
# Fix the parameters  
r = 0.05  
T = 3  
n = 100
m = 100000  # Number of paths  

# Set the random seed for reproducibility  
np.random.seed(42)  
  
class TestMonteCarloAsianOptions(unittest.TestCase):  
    def __init__(self, *args, **kwargs):  
        super(TestMonteCarloAsianOptions, self).__init__(*args, **kwargs)  
        self.results_file = 'basket_options_results.csv'  
        self.header_written = False

    def write_to_csv(self, row):  
        with open(self.results_file, mode='a', newline='') as csv_file:  
            writer = csv.writer(csv_file)  
            if not self.header_written:  
                # 写入表头  
                header = ['s1', 's2', 'K', 'T', 'sigma1', 'sigma2', 'r', 'rho', 'n', 'm', 'with_cv', 'option_type', 'value', 'lower_bound', 'upper_bound']  
                writer.writerow(header)  
                self.header_written = True  
            # 写入结果行  
            writer.writerow(row)    


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
            putFalse = [s1_i, s2_i, K_i, T, sigma1_i, sigma2_i, r, rho_i, n, m, False, 'put', mc_value, lower_bound, upper_bound]  
            self.write_to_csv(putFalse)


        for s1_p, s2_p, sigma1_p, sigma2_p, rho_p, K_p in zip(s1, s2, sigma1, sigma2, rho, K):    
            basket_vc = MonteCarloBasketVC(s1_p, s2_p, sigma1_p, sigma2_p, rho_p, r, T, K_p, n, m, 'put', True)  
        
            value_with_control_variate, lower_bound_CV, upper_bound_CV = basket_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Put option MC value with control variate should be non-negative for s1={s1_p}, s2={s2_p}, sigma1={sigma1_p}, sigma2={sigma2_p}, rho={rho_p}, K={K_p}")
            self.assertGreaterEqual(lower_bound_CV, 0, f"Put option lower_bound value with control variate should be non-negative for s1={s1_p}, s2={s2_p}, sigma1={sigma1_p}, sigma2={sigma2_p}, rho={rho_p}, K={K_p}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Put option upper_bound_CV value with control variate should be non-negative for s1={s1_p}, s2={s2_p}, sigma1={sigma1_p}, sigma2={sigma2_p}, rho={rho_p}, K={K_p}")
            putTrue = [s1_p, s2_p, K_p, T, sigma1_p, sigma2_p, r, rho_p, n, m, True, 'put', value_with_control_variate, lower_bound_CV, upper_bound_CV]  
            self.write_to_csv(putTrue)

      
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
            callFalse = [s1_j, s2_j, K_j, T, sigma1_j, sigma2_j, r, rho_j, n, m, False, 'call', mc_value, lower_bound, upper_bound]  
            self.write_to_csv(callFalse)


        for s1_q, s2_q, sigma1_q, sigma2_q, rho_q, K_q in zip(s1, s2, sigma1, sigma2, rho, K):  
            basket_vc = MonteCarloBasketVC(s1_q, s2_q, sigma1_q, sigma2_q, rho_q, r, T, K_q, n, m, 'call', True)
 
            value_with_control_variate, lower_bound_CV, upper_bound_CV = basket_vc.value_with_control_variate()  
            self.assertGreaterEqual(value_with_control_variate, 0, f"Call option price with control variate should be non-negative for s1={s1_q}, s2={s2_q}, sigma1={sigma1_q}, sigma2={sigma2_q}, rho={rho_q}, K={K_q}") 
            self.assertGreaterEqual(lower_bound_CV, 0, f"Call option lower_bound with control variate should be non-negative for s1={s1_q}, s2={s2_q}, sigma1={sigma1_q}, sigma2={sigma2_q}, rho={rho_q}, K={K_q}")  
            self.assertGreaterEqual(upper_bound_CV, 0, f"Call option upper_bound with control variate should be non-negative for s1={s1_q}, s2={s2_q}, sigma1={sigma1_q}, sigma2={sigma2_q}, rho={rho_q}, K={K_q}")   
            callTrue = [s1_q, s2_q, K_q, T, sigma1_q, sigma2_q, r, rho_q, n, m, True, 'call', value_with_control_variate, lower_bound_CV, upper_bound_CV]  
            self.write_to_csv(callTrue)


            
if __name__ == '__main__':  
    unittest.main()
