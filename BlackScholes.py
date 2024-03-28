import numpy as np
from scipy.stats import norm

N = norm.cdf


class BlackScholes(object):

    def __init__(self, s0, sigma, r, q, T, K, option_type):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type
            self.s0 = float(s0)
            self.sigma = float(sigma)
            self.T = float(T)
            self.K = float(K)
            self.r = float(r)
            self.q = float(q)
        except ValueError:
            print('Error passing Options parameters')
            raise

    def bs_call(self):
        d1 = (np.log(self.s0 / self.K) + (self.r - self.q) * (self.T)) / (self.sigma * np.sqrt(self.T)) + (
                1 / 2) * self.sigma * np.sqrt(self.T)
        d2 = (np.log(self.s0 / self.K) + (self.r - self.q) * (self.T)) / (self.sigma * np.sqrt(self.T)) - (
                1 / 2) * self.sigma * np.sqrt(self.T)

        return self.s0 * np.exp(-self.q * (self.T)) * N(d1) - self.K * np.exp(-self.r * (self.T)) * N(d2)

    def bs_put(self):
        d1 = (np.log(self.s0 / self.K) + (self.r - self.q) * (self.T)) / (self.sigma * np.sqrt(self.T)) + (
                1 / 2) * self.sigma * np.sqrt(self.T)
        d2 = (np.log(self.s0 / self.K) + (self.r - self.q) * (self.T)) / (self.sigma * np.sqrt(self.T)) - (
                1 / 2) * self.sigma * np.sqrt(self.T)

        return - self.s0 * np.exp(-self.q * (self.T)) * N(-d1) + self.K * np.exp(-self.r * (self.T)) * N(-d2)

    def get_result(self):
        if self.option_type == 'call':
            return self.bs_call()
        else:
            return self.bs_put()


# bs = BlackScholes(100, 0.3, 0.05, 0.01, 3, 100, 'put')
# print(bs.bs_put())
# print(bs.bs_asian_put())
