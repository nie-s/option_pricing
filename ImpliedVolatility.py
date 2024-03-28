import numpy as np
from scipy.stats import norm

from BlackScholes import BlackScholes

N = norm.cdf


class ImpliedVolatility(object):

    def __init__(self, s0, r, q, T, K, V, option_type):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type
            self.s0 = float(s0)
            self.T = float(T)
            self.K = float(K)
            self.r = float(r)
            self.q = float(q)
            self.V = V
            self.sigma = self.init_sigma()
        except ValueError:
            print('Error passing Options parameters')

    def init_sigma(self):
        sigma = np.sqrt(2 * abs((np.log(self.s0 / self.K) + (self.r - self.q) * (self.T)) / (self.T)))
        return sigma

    def iv_call(self):
        sigmahat = np.sqrt(2 * abs((np.log(self.s0 / self.K) + (self.r - self.q) * self.T / self.T)))
        tol = 1e-8
        nmax = 100
        sigmadiff = 1
        n = 1
        sigma = sigmahat
        while sigmadiff >= tol and n < nmax:
            bs = BlackScholes(self.s0, self.sigma, self.r, self.q, self.T, self.K, self.option_type)
            C = bs.bs_call()
            d1 = (np.log(self.s0 / self.K) + (self.r - self.q) * self.T) / (
                    self.sigma * np.sqrt(self.T)) + 0.5 * sigma * np.sqrt(self.T)

            Cvega = self.s0 * np.exp(-self.q * self.T) * np.sqrt(self.T) * N(d1)
            increment = (C - self.V) / Cvega
            sigma = sigma - increment
            if sigma < 0:
                return 'nan'
            n = n + 1
            sigmadiff = abs(increment)

        return sigma

    def iv_put(self):
        sigmahat = np.sqrt(2 * abs((np.log(self.s0 / self.K) + (self.r - self.q) * self.T / self.T)))
        tol = 1e-8
        nmax = 100
        sigmadiff = 1
        n = 1
        sigma = sigmahat

        while sigmadiff >= tol and n < nmax:
            bs = BlackScholes(self.s0, self.sigma, self.r, self.T, self.K, self.option_type)
            P = bs.bs_put()
            d1 = (np.log(self.s0 / self.K) + (self.r - self.q) * self.T) / (
                    self.sigma * np.sqrt(self.T)) + 0.5 * sigma * np.sqrt(self.T)

            Pvega = self.s0 * np.exp(-self.q * self.T) * np.sqrt(self.T) * N(d1)
            increment = (P - self.V) / Pvega
            sigma = sigma - increment
            n = n + 1
            sigmadiff = abs(increment)

        return sigma

    def get_result(self):
        if self.option_type == 'call':
            return self.iv_call()
        else:
            return self.iv_put()
