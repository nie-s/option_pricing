import numpy as np
import pandas as pd
from scipy.stats import norm, qmc

class QMonteCarloKIKOPut:
    def __init__(self, s0, K, L, U, R, r, sigma0, T, m, seed, n):
        self.s0 = s0  # Current stock price
        self.K = K  # Strike price
        self.L = L  # Lower barrier
        self.U = U  # Upper barrier
        self.R = R  # Rebate payment
        self.r = r  # Risk-free rate
        self.sigma0 = sigma0  # Volatility
        self.T = T  # Maturity
        self.m = m  # Number of samples
        self.n = n  # Number of observation time
        self.delta_t = T / n  # Time step size
        self.seed = seed

    def simulate_stock_path(self):
        stock_path = np.zeros((self.n + 1, self.m))
        stock_path[0, :] = self.s0

        for i in range(self.n):
            sobol = qmc.Sobol(d=1, seed=self.seed)
            X = np.array(sobol.random(n=self.m))
            wt = norm.ppf(X)
            stock_path[i + 1, :] = (
                stock_path[i, :] * np.exp(
                    (self.r - 0.5 * self.sigma0 ** 2) * self.delta_t +
                    self.sigma0 * np.sqrt(self.delta_t) * wt.T[:, ]
                )
            )

        return pd.DataFrame(stock_path)

    def calculate_option_price(self):
        df = self.simulate_stock_path()

        terminaltime = np.zeros((1, self.m))
        terminalpayoff = np.zeros((1, self.m))
        terminalstatus = np.zeros((1, self.m))

        for i in range(self.m):
            for j in range(1, self.n + 1):
                price = df.iloc[j, i]

                if price > self.U:
                    terminalstatus[0, i] = 1
                    terminaltime[0, i] = j
                    terminalpayoff[0, i] = self.R
                    break

                if price <= self.L:
                    terminalstatus[0, i] = -1

            if terminalstatus[0, i] == -1:
                terminaltime[0, i] = j
                terminalpayoff[0, i] = max(self.K - df.iloc[j, i], 0)

            if terminalstatus[0, i] == 0:
                terminaltime[0, i] = j
                terminalpayoff[0, i] = 0

        option_price = np.mean(
            terminalpayoff * np.exp(-self.r * terminaltime * self.delta_t / self.T)
        )

        return option_price
    
    def kiko_put_option_price_delta(self, e=0.01):
        p0 = self.calculate_option_price()
        p1 = QMonteCarloKIKOPut(self.s0 * (1 + e / 2), self.K, self.L, self.U, self.R, self.r, self.sigma0, self.T, self.m, self.seed, self.n).calculate_option_price()
        p2 = QMonteCarloKIKOPut(self.s0 * (1 - e / 2), self.K, self.L, self.U, self.R, self.r, self.sigma0, self.T, self.m, self.seed, self.n).calculate_option_price()
        delta = (p1 - p2) / (self.s0 * e)
        return delta
    
    def calculate_price_and_delta(self):
        option_price = self.calculate_option_price()
        delta = self.kiko_put_option_price_delta()
        return option_price,delta
    
    def get_result(self):
        option_price = self.calculate_option_price()


