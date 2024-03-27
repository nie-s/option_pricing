import numpy as np  
import math  
from scipy.stats import norm, qmc  
  
class QMonteCarloKIKOPut(object):  
    def __init__(self, S0, sigma, r, T, K, L, U, R, n, seed):  
        self.S0 = S0  
        self.sigma = sigma  
        self.r = r  
        self.T = T  
        self.K = K  
        self.L = L  
        self.U = U  
        self.R = R  
        self.n = n  
        self.seed = seed  
  

    def kiko_put_payoff(self, s):  
        """KIKO put option payoff function."""  
        if self.L <= s <= self.U:  
            return max(0, self.K - s)  
        else:  
            return self.R  

    def calculate_price(self, M, S0):  
        ##if S0 is None:  
        ##   S0 = self.S0

        factor = self.S0 * np.exp((self.r - 0.5 * self.sigma**2) * self.T)  
        std = self.sigma * math.sqrt(self.T)  
        sequencer = qmc.Sobol(d=1, seed=self.seed)  
        X = np.array(sequencer.random(n=M))  
        Z = norm.ppf(X)  
        sArray = factor * np.exp(std * Z)  
        payoffArray = np.array([self.kiko_put_payoff(s) for s in sArray], dtype=object)  
        option_price = np.mean(payoffArray) * np.exp(-self.r * self.T)  
        return option_price
    

    def calculate_price_and_delta(self, M):  
        """Calculate the price and Delta of a KIKO put option using Quasi-Monte Carlo."""  
        # Calculate standard deviation and factor  
        factor = self.S0 * np.exp((self.r - 0.5 * self.sigma**2) * self.T) 
        std = self.sigma * math.sqrt(self.T)  
  
        # Initialize Sobol sequence generator  
        sequencer = qmc.Sobol(d=1, seed=self.seed)  
  
        # Generate quasi-random numbers  
        X = np.array(sequencer.random(n=M))  
        Z = norm.ppf(X)  # Transform to normal distribution  
  
        # Calculate the future stock prices  
        sArray = factor * np.exp(std * Z)  
  
        # Calculate the payoffs  
        payoffArray = np.array([self.kiko_put_payoff(s) for s in sArray], dtype=object)
        ##assert payoffArray.ndim == 1
  
        # Calculate the option price  
        option_price = np.mean(payoffArray) * np.exp(-self.r * self.T)  
  
        # Calculate Delta using finite difference  
        ##up_shift = 1e-3 * self.S0  # 向上平移的量  
        ##option_price_up = self.calculate_price(M, self.S0 + up_shift)  
        ##delta = (option_price_up - option_price) / up_shift 

        up_shift = 1e-4 * self.S0  # 向上平移的量  
        down_shift = -up_shift     # 向下平移的量  
        option_price_up = self.calculate_price(M, self.S0 + up_shift)  
        option_price_down = self.calculate_price(M, self.S0 + down_shift)  
        delta = (option_price_up - option_price_down) / (2 * up_shift)
        return option_price, delta  
        
  
    def calculate_price_and_delta_with_errors(self, Ms, Ctrue):  
        """Calculate the prices and errors for multiple sample sizes."""  
        aMList = []  
        aDeltaList = []
        aMErrorList = []  
  
        for M in Ms:  
            option_price, delta = self.calculate_price_and_delta(int(M))  
            aMList.append(option_price)  
            aDeltaList.append(delta)  # 添加delta到列表  
            aMErrorList.append(Ctrue - option_price)  # 假设Ctrue是真实价格  
  
        return aMList, aDeltaList, aMErrorList  # 返回包含期权价格、delta和误差的元组


# Example usage:  
# Define the parameters for the KIKO put option  
S0 = 100.0  # Initial stock price  
sigma = 0.2  # Volatility  
r = 0.05  # Risk-free rate  
T = 1.0  # Time to maturity (in years)  
K = 100.0  # Strike price  
L = 90.0  # Lower barrier  
U = 110.0  # Upper barrier  
R = 5.0  # Cash rebate  
n = 100  # Number of observation times (not used in this example)  
seed = 200  # Random seed for reproducibility  
  
# True price (replace with an appropriate value or omit for error calculation)  
Ctrue = 10.0  # This should be replaced with the true price or a benchmark  
  
# Create an instance of the QMonteCarloKIKOPut class  
qmc_kiko_put = QMonteCarloKIKOPut(S0, sigma, r, T, K, L, U, R, n, seed)  
  
# Calculate the option price and Delta for a given number of samples  
M = 100000  # Number of quasi-random samples  
option_price, delta = qmc_kiko_put.calculate_price_and_delta(M)

print("Using", M ,"samples:")  
print("KIKO Put Option Price:",option_price)  
print("KIKO Put Option Delta:",delta)
