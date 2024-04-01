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

How Strike Price Affects Put Option price

"""

s0 = 50
L = 40
U = 140
R = 10
r = 0.01
sigma0 = 0.2
T = 1.0
m = 10**5
n = 50
price=[]
param=[]
for K in range(10,100,10):
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(K)

plt.plot(param,price)
# naming the x axis
plt.xlabel('Strike Price')
# naming the y axis
plt.ylabel('KIKO Put Option Price')
plt.title(title+' Put Option')
plt.show()


"""

How Maturity Affects Put Option Price

"""

s0 = 50
K= 50
L = 40
U = 140
R = 10
r = 0.01
sigma0 = 0.2
n = 50
m = 10**5
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
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()


"""

How Volatility Affects Put Option Price

"""

fig, ax = plt.subplots(3, sharex=True, figsize=[11, 9])
fig.suptitle(title+ ' KIKO Put Option')
fig.align_labels()

s0 = 50
K= 60
L = 40
U = 140
R = 10
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma0 in range(1,100,1):
    sigma0 = sigma0 * 0.01
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(sigma0)
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Put Option price')

s0 = 50
K = 50
L = 40
U = 140
R = 10
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma * 0.01
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(sigma)
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Put Option price')

s0 = 50
K = 35.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma=sigma*0.01
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(sigma)
ax[2].plot(param,price, label = 'OTM', color='g')
ax[2].set_ylabel('Put Option price')


fig.legend(loc='upper left')
plt.xlabel('Volatility')
plt.show()


"""

How Risk Free Rate Affects Put Option Price

"""

s0 = 50
K = 50
L = 40
U = 140
R = 10
sigma0 = 0.2
n = 50
m = 10**5
price=[]
param=[]
for r in range(1,40,1):
    r = r * 0.01
    C = QMonteCarloKIKOPut(s0, K, L, U, R, r, sigma0, T, m, n)
    price.append(C.calculate_price_and_delta())
    param.append(r)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Risk Free Rate')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()


"""

How Number of Observation Times Affects Put Option Price

"""

s0 = 50
K = 50.5
L = 40
U = 140
R = 10
sigma = 0.2
r = 0.01
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
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()
