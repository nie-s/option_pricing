import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from QMonteCarloKIKOPut import QMonteCarloKIKOPut   
title = 'QMA KIKO Put'


"""

How Current Price Affects Put Option price

"""

K = 9
L = 9.3
U = 10.2
R = 5
r = 0.06
sigma0 = 0.1
T = 1.0
m = 10**5
n = 10
price=[]
param=[]
for s0 in range(95,105,1):
    s0 = s0 * 0.1
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(s0)

plt.plot(param,price)
# naming the x axis
plt.xlabel('Current Price')
# naming the y axis
plt.ylabel('KIKO Put Option Price')
plt.title(title+' Option')
plt.show()


"""

How Maturity Affects Put Option Price

"""

s0 = 10
K = 9
L = 9.3
U = 10.2
R = 5
r = 0.06
sigma0 = 0.1
m = 10**5
n = 10
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(T)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Maturity')
# naming the y axis
plt.ylabel('KIKO Put Option Price')
plt.title(title+ ' Option')
plt.show()


"""

How Risk Free Rate Affects Put Option Price

"""

s0 = 10
K = 9
L = 9.3
U = 10.2
R = 5
sigma0 = 0.1
m = 10**5
n = 10
price=[]
param=[]
for r in range(1,9,1):
    r = r * 0.01
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(r)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Risk Free Rate')
# naming the y axis
plt.ylabel('KIKO Put Option Price')
plt.title(title+ ' Option')
plt.show()


"""

How Number of Observation Times Affects Put Option Price

"""

s0 = 10
K = 9
L = 9.3
U = 10.2
R = 5
r = 0.06
sigma0 = 0.1
m = 10**5
price=[]
param=[]
for n in range(10,500):
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(n)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Observation Time Steps')
# naming the y axis
plt.ylabel('KIKO Put Option Price')
plt.title(title+ ' Option')
plt.show()
