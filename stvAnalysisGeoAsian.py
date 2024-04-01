import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from MonteCarloAsianVC import MonteCarloAsianVC   
title = 'Geometric Asian'


"""

How Strike Price Affects Call Option Price

"""

s0 = 50
t = 0
T = 0.5
sigma = 0.2
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for K in range(10,100,10):
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'call', True)
    price.append(C.asian_geo())
    param.append(K)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Strike Price')
# naming the y axis
plt.ylabel('Call Option Price')
plt.title(title+' Call Option')
plt.show()


"""

How Strike Price Affects Put Option Price

"""

s0 = 50
t = 0
T = 0.5
sigma = 0.2
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for K in range(10,100,10):
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'put', True)
    price.append(C.asian_geo())
    param.append(K)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Strike Price')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+' Put Option')
plt.show()


"""

How Maturity Affects Call Option Price

"""

s0 = 50
K = 50
t = 0
sigma = 0.2
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'call', True)
    price.append(C.asian_geo())
    param.append(T)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Maturity')
# naming the y axis
plt.ylabel('Call Option Price')
plt.title(title+ ' Call Option')
plt.show()


"""

How Maturity Affects Put Option Price

"""

s0 = 50
K = 50
t = 0
sigma = 0.2
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'put', True)
    price.append(C.asian_geo())
    param.append(T)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Maturity')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()


"""

How Volatility Affects Call Option Price

"""

fig, ax = plt.subplots(3, sharex=True, figsize=[11, 9])

fig.suptitle(title+ ' Call Option')
fig.align_labels()

s0 = 50
K= 35
t = 0
T = 0.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'call', True)
    price.append(C.asian_geo())
    param.append(sigma)   
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Call Option price')

s0 = 50
K= 50
t = 0
T=0.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'call', True)
    price.append(C.asian_geo())
    param.append(sigma)
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Call Option price')

s0 = 50
K= 55
t = 0
T=0.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma  * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'call', True)
    price.append(C.asian_geo())
    param.append(sigma)
ax[2].plot(param,price, label='OTM',color='g')
ax[2].set_ylabel('Call Option price')

fig.legend(loc='upper left')
plt.xlabel('Volatility')
plt.show()


"""

How Volatility Affects Put Option Price

"""

fig, ax = plt.subplots(3, sharex=True, figsize=[11, 9])

fig.suptitle(title+ ' Put Option')
fig.align_labels()

s0 = 50
K= 60
t = 0
T = 0.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'put', True)
    price.append(C.asian_geo())
    param.append(sigma)   
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Call Option price')

s0 = 50
K= 50
t = 0
T=0.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'put', True)
    price.append(C.asian_geo())
    param.append(sigma)
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Put Option price')

s0 = 50
K= 35
t = 0
T=0.5
r = 0.01
n = 50
m = 10**5
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'put', True)
    price.append(C.asian_geo())
    param.append(sigma)
ax[2].plot(param,price, label='OTM',color='g')
ax[2].set_ylabel('Put Option price')

fig.legend(loc='upper left')
plt.xlabel('Volatility')
plt.show()


"""

How Risk Free Rate Affects Call Option Price

"""

s0 = 50
K= 50
t = 0
T = 0.5
sigma = 0.2
n = 50
m = 10**5
price=[]
param=[]
for r in range(1,40,1):
    r = r * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'call', True)
    price.append(C.asian_geo())
    param.append(r)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Risk Free Rate')
# naming the y axis
plt.ylabel('Call Option Price')
plt.title(title+ ' Call Option')
plt.show()


"""

How Risk Free Rate Affects Put Option Price

"""

s0 = 50
K= 50
t = 0
T = 0.5
sigma = 0.2
n = 50
m = 10**5
price=[]
param=[]
for r in range(1,40,1):
    r = r * 0.01
    C = MonteCarloAsianVC(s0, sigma, r, T, K, n, m, 'put', True)
    price.append(C.asian_geo())
    param.append(r)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Risk Free Rate')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()
