import math

import numpy as np
from scipy.stats import norm

N = norm.cdf


class ClosedFormAsian(object):

    def __init__(self, s0, sigma, r, T, K, n, option_type):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type
            self.s0 = float(s0)
            self.sigma = float(sigma)
            self.T = float(T)
            self.K = float(K)
            self.r = float(r)
            self.n = int(n)
        except ValueError:
            print('Error passing Options parameters')
            raise

    def cf_asian_call(self):
        sigma_hat = self.sigma * math.sqrt(((self.n + 1) * (2 * self.n + 1)) / (6 * self.n ** 2))
        mu = (self.r - (1 / 2) * self.sigma ** 2) * ((self.n + 1) / (2 * self.n)) + (1 / 2) * sigma_hat ** 2

        d1 = ((math.log(self.s0 / self.K) + (mu + (1 / 2) * sigma_hat ** 2)) * self.T) / (sigma_hat * math.sqrt(self.T))
        d2 = d1 - sigma_hat * math.sqrt(self.T)

        call = np.exp(-(self.r * self.T)) * (self.s0 * np.exp(mu * self.T) * N(d1) - self.K * N(d2))

        return call

    # for put option
    def cf_asian_put(self):
        sigma_hat = self.sigma * math.sqrt(((self.n + 1) * (2 * self.n + 1)) / (6 * self.n ** 2))
        mu = (self.r - (1 / 2) * self.sigma ** 2) * ((self.n + 1) / (2 * self.n)) + (1 / 2) * sigma_hat ** 2

        d1 = ((math.log(self.s0 / self.K) + (mu + (1 / 2) * sigma_hat ** 2)) * self.T) / (sigma_hat * math.sqrt(self.T))
        d2 = d1 - sigma_hat * math.sqrt(self.T)

        # the closed-form formulas for geometric Asian put option
        put = np.exp(-(self.r * self.T)) * (self.K * N(-d2) - self.s0 * np.exp(mu * self.T) * N(-d1))

        return put

    def get_result(self):
        if self.option_type == 'call':
            return self.cf_asian_call()
        else:
            return self.cf_asian_put()
