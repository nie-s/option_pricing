import numpy as np
from scipy.stats import norm

N = norm.cdf


class CloasedFormBasket(object):

    def __init__(self, s1, s2, sigma1, sigma2, rho, r, T, K, option_type):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type

            self.s1 = float(s1)
            self.s2 = float(s2)
            self.sigma1 = float(sigma1)
            self.sigma2 = float(sigma2)

            self.rho = rho
            self.T = float(T)
            self.K = float(K)
            self.r = float(r)
        except ValueError:
            print('Error passing Options parameters')

    def cf_basket_call(self):
        v = 1 / 2 * np.sqrt((self.sigma1 ** 2) + 2 * self.sigma1 * self.sigma2 * self.rho + self.sigma2 ** 2)
        mu = self.r - (1 / 2) * ((self.sigma1 ** 2 + self.sigma2 ** 2) / 2) + (1 / 2) * v ** 2

        S = np.sqrt(self.s1 * self.s2)

        d1 = (np.log(S / self.K) + (mu + (1 / 2) * v ** 2) * self.T) / (v * np.sqrt(self.T))
        d2 = d1 - v * np.sqrt(self.T)

        return np.exp(-(self.r * self.T)) * (S * np.exp(mu * self.T) * N(d1) - self.K * N(d2))

    def cf_basket_put(self):
        v = 1 / 2 * np.sqrt((self.sigma1 ** 2) + 2 * self.sigma1 * self.sigma2 * self.rho + self.sigma2 ** 2)
        mu = self.r - (1 / 2) * ((self.sigma1 ** 2 + self.sigma2 ** 2) / 2) + (1 / 2) * v ** 2

        S = np.sqrt(self.s1 * self.s2)

        d1 = (np.log(S / self.K) + (mu + (1 / 2) * v ** 2) * self.T) / (v * np.sqrt(self.T))
        d2 = d1 - v * np.sqrt(self.T)

        return np.exp(-(self.r * self.T)) * (-S * np.exp(mu * self.T) * N(-d1) + self.K * N(-d2))


myBSbasket = CloasedFormBasket(4, 5, 0.25, 0.2, 0.03, 0.2, 1, 4, 'call')
print(myBSbasket.cf_basket_call())
