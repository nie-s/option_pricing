import numpy as np


class BionomalTreeAmerican(object):

    def __init__(self, s0, sigma, r, T, K, n, option_type):
        try:
            assert option_type == 'call' or option_type == 'put'
            self.option_type = option_type
            self.s0 = float(s0)
            self.sigma = float(sigma)
            self.T = float(T)
            self.K = float(K)
            self.n = int(n)
            self.r = float(r)

            self.deltat = float(T) / n
            self.u = np.exp(sigma * np.sqrt(self.deltat))
            self.d = np.exp(-sigma * np.sqrt(self.deltat))
            self.dt = T / n

        except ValueError:
            print('Error passing Options parameters')

    def american_fast_tree(self):
        # precompute values
        q = (np.exp(self.r * self.dt) - self.d) / (self.u - self.d)
        disc = np.exp(-self.r * self.dt)

        # initialise stock prices at maturity
        S = self.s0 * self.d ** (np.arange(self.n, -1, -1)) * self.u ** (np.arange(0, self.n + 1, 1))

        # option payoff
        if self.option_type == 'put':
            C = np.maximum(0, self.K - S)
        else:
            C = np.maximum(0, S - self.K)

        # backward recursion through the tree
        for i in np.arange(self.n - 1, -1, -1):
            S = self.s0 * self.d ** (np.arange(i, -1, -1)) * self.u ** (np.arange(0, i + 1, 1))
            C[:i + 1] = disc * (q * C[1:i + 2] + (1 - q) * C[0:i + 1])
            C = C[:-1]
            if self.option_type == 'put':
                C = np.maximum(C, self.K - S)
            else:
                C = np.maximum(C, S - self.K)

        return C[0]


my_american_tree = BionomalTreeAmerican(100, 0.2, 0.06, 1, 100, 3, 'put')
print(my_american_tree.american_fast_tree())
