import numpy as np
from scipy.stats import norm

N = norm.cdf


class MonteCarloBasketVC(object):

    def __init__(self, s1, s2, sigma1, sigma2, rho, r, T, K, n, m, option_type):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type
            self.s1 = float(s1)
            self.s2 = float(s2)
            self.sigma1 = float(sigma1)
            self.sigma2 = float(sigma2)
            self.T = float(T)
            self.K = float(K)
            self.rho = float(rho)
            self.n = int(n)
            self.m = int(m)
            self.r = float(r)

        except ValueError:
            print('Error passing Options parameters')

        # if option_type != 'call' and option_type != 'put':
        #     raise ValueError("Error: option type not valid. Enter 'call' or 'put'")
        # if s0 < 0 or K < 0 or T <= 0 or r < 0 or sigma < 0:
        #     raise ValueError('Error: Negative inputs not allowed')

        self.dt = self.T / float(self.n)
        self.discount = np.exp(- self.r * self.T)

    def basket_geo(self):
        sigsqT = (self.sigma1 ** 2 + 2 * self.sigma1 * self.sigma2 * self.rho + self.sigma2 ** 2) / (2 ** 2)
        # mu multiply by T
        self.muT = (self.r - 0.5 * ((self.sigma1 ** 2 + self.sigma2 ** 2) / 2) + 0.5 * sigsqT) * self.T
        self.Bg0 = np.sqrt(self.s1 * self.s2)

        self.d1 = (np.log(self.Bg0 / self.K) + (self.muT + 1 / 2 * sigsqT * self.T)) / (
                np.sqrt(sigsqT) * np.sqrt(self.T))
        self.d2 = self.d1 - np.sqrt(sigsqT) * np.sqrt(self.T)

        drift_1 = np.exp((self.r - 0.5 * self.sigma1 ** 2) * self.T)
        drift_2 = np.exp((self.r - 0.5 * self.sigma2 ** 2) * self.T)

        Z_1 = np.random.normal(0, 1, 1)
        # mu = 0, sigma = 1, X1, X2 are i.i.d
        # Y1 = mu + sigmaX1, Y2 = mu + sigma(rhoX1 + sqrt(1-rho**2*X2))
        Z_2 = self.rho * Z_1 + np.sqrt(1 - self.rho ** 2) * np.random.normal(0, 1, 1)
        geo1 = self.s1 * drift_1 * np.exp(self.sigma1 * np.sqrt(self.T) * Z_1)
        geo2 = self.s2 * drift_2 * np.exp(self.sigma2 * np.sqrt(self.T) * Z_2)

        return geo1, geo2

    def price_paths(self, seed=100):
        np.random.seed(seed)
        price_path1 = (self.s1 * np.cumprod(
            np.exp((self.r - 0.5 * self.sigma1 ** 2) * self.dt +
                   self.sigma1 * np.sqrt(self.dt) * np.random.randn(self.m, self.n)), 1))

        price_path2 = (self.s2 * np.cumprod(
            np.exp((self.r - 0.5 * self.sigma2 ** 2) * self.dt +
                   self.sigma2 * np.sqrt(self.dt) * np.random.randn(self.m, self.n)), 1))

        return price_path1, price_path2

    def mc_payoff(self):
        geo1, geo2 = self.basket_geo()
        ave = 1 / 2 * (geo2 + geo1)
        if self.option_type == 'call':
            mc_payoff = self.discount * np.maximum(ave - self.K, 0)
        else:
            mc_payoff = self.discount * np.maximum(self.K - ave, 0)
        return mc_payoff

    def value(self):
        mc_value = np.mean(self.mc_payoff())
        mc_value_std = np.std(self.mc_payoff())
        upper_bound = mc_value + 1.96 * mc_value_std / np.sqrt(self.m)
        lower_bound = mc_value - 1.96 * mc_value_std / np.sqrt(self.m)

        return mc_value, lower_bound, upper_bound

    def value_with_control_variate(self):
        path1, path2 = self.price_paths()

        # geometric_average = np.exp((1 / float(self.n)) * 1 / 2 * (np.sum(np.log(path1), 1) + np.sum(np.log(path2), 1)))
        # geometric_average = np.exp((1 / float(self.n)) * np.log(path1 + path2))

        # print(geometric_average)
        geo1, geo2 = self.basket_geo()
        geoMean = np.exp((1 / 2) * (np.log(geo1) + np.log(geo2)))

        geo_payoff_call = np.exp(-self.r * self.T) * max(geoMean - self.K, 0)
        geo_payoff_put = np.exp(-self.r * self.T) * max(self.K - geoMean, 0)

        mc_payoff = self.mc_payoff()
        Bg0 = np.sqrt(self.s1 * self.s2)

        ### Control variate version
        if self.option_type == 'call':
            # implement the closed-from formula for Geometric Mean Basket Call Option
            geo_call = np.exp(-self.r * self.T) * (Bg0 * np.exp(self.muT) * N(self.d1) - self.K * N(self.d2))
            value_with_CV = mc_payoff + geo_call - geo_payoff_call

        else:
            # implement the closed-from formula for Geometric Mean Basket Put Option
            geo_put = np.exp(-self.r * self.T) * (self.K * N(-self.d2) - Bg0 * np.exp(self.muT) * N(-self.d1))
            value_with_CV = mc_payoff + geo_put - geo_payoff_call

        value_with_control_variate = np.mean(value_with_CV, 0)
        value_with_control_variate_std = np.std(value_with_CV, 0)

        upper_bound_CV = value_with_control_variate + 1.96 * value_with_control_variate_std / np.sqrt(self.m)
        lower_bound_CV = value_with_control_variate - 1.96 * value_with_control_variate_std / np.sqrt(self.m)
        return value_with_control_variate, lower_bound_CV, upper_bound_CV


myBasketCall = MonteCarloBasketVC(4, 5, 0.25, 0.2, 0.03, 0.2, 1, 1, 100, 10000, 'call')
print(myBasketCall.value())
print(myBasketCall.value_with_control_variate())
