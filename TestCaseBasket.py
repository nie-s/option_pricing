import unittest  
import numpy as np  
from scipy.stats import norm  
from MonteCarloBasket import MonteCarloBasketVC  
   
  
# 设定测试案例  
test_cases = [  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'put'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.9, 'option_type': 'put'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.1, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'put'},  
    {'s1': 100, 's2': 100, 'K': 80,  'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'put'},  
    {'s1': 100, 's2': 100, 'K': 120, 'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'put'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.5, 'sigma2': 0.5, 'rho': 0.5, 'option_type': 'put'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'call'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.9, 'option_type': 'call'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.1, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'call'},  
    {'s1': 100, 's2': 100, 'K': 80,  'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'call'},  
    {'s1': 100, 's2': 100, 'K': 120, 'sigma1': 0.3, 'sigma2': 0.3, 'rho': 0.5, 'option_type': 'call'},  
    {'s1': 100, 's2': 100, 'K': 100, 'sigma1': 0.5, 'sigma2': 0.5, 'rho': 0.5, 'option_type': 'call'}  
]  

np.random.seed(42) 

class TestMonteCarloBasket(unittest.TestCase): 
    def setUp(self):  
        # 通用参数  
        self.r = 0.05  
        self.T = 3  
        self.S0 = 100  
        self.m = 100000
        self.n = 100  

    def test_put_basket(self):  
        for case in test_cases:   
            mc_basket = MonteCarloBasketVC(  
                s1=case['s1'], s2=case['s2'], K=case['K'],  
                sigma1=case['sigma1'], sigma2=case['sigma2'], rho=case['rho'],  
                r=self.r, T=self.T, n=self.n, m=self.m, option_type=case['option_type']  
            ) 

            value_mc = mc_basket.value()  
            value_cv = mc_basket.value_with_control_variate()  

            self.assertIsInstance(value_mc, tuple)  
            self.assertIsInstance(value_cv, tuple)
            
            print(f"Test case: {case}") 

            # 打印 Monte Carlo Value  
            print(f"Monte Carlo Value:")  
            for idx, val in enumerate(value_mc):  
                print(f"  Element {idx}: {val:.4f}")  
  
            # 打印 Monte Carlo Value with Control Variate  
            print(f"Monte Carlo Value with Control Variate:")  
            for idx, val in enumerate(value_cv):  
                print(f"Element {idx}: {val:.4f}")    


if __name__ == '__main__':  
    unittest.main()        
