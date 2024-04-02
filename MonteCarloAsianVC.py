import numpy as np
from scipy.stats import norm

N = norm.cdf


class MonteCarloAsianVC(object):

    def __init__(self, s0, sigma, r, T, K, n, m, option_type, control):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type
            self.s0 = float(s0)
            self.sigma = float(sigma)
            self.T = float(T)
            self.K = float(K)
            self.n = int(n)
            self.m = int(m)
            self.r = float(r)
            self.control = control

        except ValueError:
            print('Error passing Options parameters')
            raise

        # if option_type != 'call' and option_type != 'put':
        #     raise ValueError("Error: option type not valid. Enter 'call' or 'put'")
        # if s0 < 0 or K < 0 or T <= 0 or r < 0 or sigma < 0:
        #     raise ValueError('Error: Negative inputs not allowed')

        self.dt = self.T / float(self.n)
        self.discount = np.exp(- self.r * self.T)

    def asian_geo(self):
        sigsqT = ((self.sigma ** 2 * self.T * (self.n + 1) * (2 * self.n + 1)) / (6 * self.n * self.n))
        muT = (0.5 * sigsqT + (self.r - 0.5 * self.sigma ** 2)
               * self.T * (self.n + 1) / (2 * self.n))
        d1 = ((np.log(self.s0 / self.K) + (muT + 0.5 * sigsqT))
              / np.sqrt(sigsqT))
        d2 = d1 - np.sqrt(sigsqT)
        if self.option_type == 'call':
            geometric_value = self.discount * (self.s0 * np.exp(muT) * N(d1) - self.K * N(d2))
        else:
            geometric_value = self.discount * (-self.s0 * np.exp(muT) * N(-d1) + self.K * N(-d2))

        return geometric_value

    def price_path(self, seed=100):
        np.random.seed(seed)
        price_path = (self.s0 *
                      np.cumprod(np.exp((self.r - 0.5 * self.sigma ** 2) * self.dt + self.sigma * np.sqrt(self.dt)
                                        * np.random.randn(self.m, self.n)), 1))
        return price_path

    def mc_payoff(self):
        if self.option_type == 'call':
            mc_payoff = self.discount * np.maximum(np.mean(self.price_path(), 1) - self.K, 0)
        else:
            mc_payoff = self.discount * np.maximum(self.K - np.mean(self.price_path(), 1), 0)
        return mc_payoff

    def value(self):
        mc_value = np.mean(self.mc_payoff())
        mc_value_std = np.std(self.mc_payoff())
        upper_bound = mc_value + 1.96 * mc_value_std / np.sqrt(self.m)
        lower_bound = mc_value - 1.96 * mc_value_std / np.sqrt(self.m)
        print(mc_value, lower_bound, upper_bound)
        return mc_value, lower_bound, upper_bound

    def value_with_control_variate(self):

        geometric_average = np.exp((1 / float(self.n)) * np.sum(np.log(self.price_path()), 1))
        print(geometric_average)

        if self.option_type == 'call':
            mc_payoff_geo = self.discount * np.maximum(geometric_average - self.K, 0)
            value_with_CV = self.mc_payoff() + self.asian_geo() - mc_payoff_geo
        else:
            mc_payoff_geo = self.discount * np.maximum(self.K - geometric_average, 0)
            value_with_CV = self.mc_payoff() + self.asian_geo() - mc_payoff_geo

        value_with_control_variate = np.mean(value_with_CV, 0)
        value_with_control_variate_std = np.std(value_with_CV, 0)

        upper_bound_CV = value_with_control_variate + 1.96 * value_with_control_variate_std / np.sqrt(self.m)
        lower_bound_CV = value_with_control_variate - 1.96 * value_with_control_variate_std / np.sqrt(self.m)
        return value_with_control_variate, lower_bound_CV, upper_bound_CV

    def get_result(self):
        if self.control == True:
            return self.value()
        else:
            return self.value_with_control_variate()


myAsianCall = MonteCarloAsianVC(4, 0.25, 0.03, 1, 4, 100, 10000, 'call', True)
# print(myAsianCall.value())
print(myAsianCall.value_with_control_variate())
