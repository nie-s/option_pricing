import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from MonteCarloBasket import MonteCarloBasketVC
title= 'Monte Carlo Basket'


"""

How Strike Price Affects Call Option Price

"""

s1 = 50
s2 = 50
t = 0
T = 0.5
sigma1 = 0.3
sigma2 = 0.3
r = 0.01
rho = 0.5
m = 10**5
n = 100
price=[]
param=[]
for K in range(10,100,10):
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
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

s1 = 50
s2 = 50
t = 0
T = 0.5
sigma1 = 0.3
sigma2 = 0.3
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]
for K in range(10,100,10):
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
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

s1 = 50
s2 = 50
K = 50
t = 0
sigma1 = 0.3
sigma2 = 0.3
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
    param.append(T)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Maturity')
# naming the y axis
plt.ylabel('Call Option Price')
plt.title(title+' Call Option')
plt.show()


"""

How Maturity Affects Put Option Price

"""

s1 = 50
s2 = 50
K = 50
t = 0
sigma1 = 0.3
sigma2 = 0.3
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
    param.append(T)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Maturity')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+' Put Option')
plt.show()


"""

How Volatility Affects Call Option Price

"""

fig, ax = plt.subplots(3, sharex=True, figsize=[11, 9])

fig.suptitle(title+ 'Option ')
fig.align_labels()

s1 = 50
s2 = 50
K= 38
T = 0.5
t = 0
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]

for sigma_val in np.arange(0.01, 1.0, 0.01):  # 生成一个从0.01到0.99的数组，步长为0.01  
    sigma1 = sigma_val  
    sigma2 = sigma_val
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
    param.append(sigma_val)  
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Call Option price')

s1 = 50
s2 = 50
K= 50
t = 0
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]
price=[]
param=[]
for sigma_val in np.arange(0.01, 1.0, 0.01):  # 生成一个从0.01到0.99的数组，步长为0.01  
    sigma1 = sigma_val  
    sigma2 = sigma_val
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
    param.append(sigma_val)
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Call Option price')

s1 = 50
s2 = 50
K= 60
t = 0
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]
price=[]
param=[]
for sigma_val in np.arange(0.01, 1.0, 0.01):  # 生成一个从0.01到0.99的数组，步长为0.01  
    sigma1 = sigma_val  
    sigma2 = sigma_val
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
    param.append(sigma_val)
ax[2].plot(param,price, label='OTM',color='g')
ax[2].set_ylabel('Call Option price')

fig.legend(loc='upper left')
plt.xlabel('Volatility')
plt.show()


"""

How Volatility Affects Put Option Price

"""

fig, ax = plt.subplots(3, sharex=True, figsize=[11, 9])

fig.suptitle(title+ 'Option ')
fig.align_labels()

s1 = 50
s2 = 50
K= 60
T = 0.5
t = 0
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]

for sigma_val in np.arange(0.01, 1.0, 0.01):  # 生成一个从0.01到0.99的数组，步长为0.01  
    sigma1 = sigma_val  
    sigma2 = sigma_val
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
    param.append(sigma_val)  
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Put Option price')

s1 = 50
s2 = 50
K= 50
t = 0
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]

for sigma_val in np.arange(0.01, 1.0, 0.01):  # 生成一个从0.01到0.99的数组，步长为0.01  
    sigma1 = sigma_val  
    sigma2 = sigma_val
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
    param.append(sigma_val) 
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Put Option price')

s1 = 50
s2 = 50
K= 40
t = 0
r = 0.01
rho = 0.5
m = 10**5
price=[]
param=[]

for sigma_val in np.arange(0.01, 1.0, 0.01):  # 生成一个从0.01到0.99的数组，步长为0.01  
    sigma1 = sigma_val  
    sigma2 = sigma_val
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
    param.append(sigma_val) 
ax[2].plot(param,price, label='OTM',color='g')
ax[2].set_ylabel('Put Option price')

fig.legend(loc='upper left')
plt.xlabel('Volatility')
plt.show()


"""

How Risk Free Rate Affects Call Option Price

"""

s1 = 50
s2 = 50
K = 50
t = 0
T = 0.5
sigma1 = 0.3
sigma2 = 0.3
rho = 0.5
m = 10**5
price=[]
param=[]
for r in range(1,40,1):
    r = r*0.01
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
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

s1 = 50
s2 = 50
K = 50
t = 0
T = 0.5
sigma1 = 0.3
sigma2 = 0.3
rho = 0.5
m = 10**5
price=[]
param=[]
for r in range(1,40,1):
    r = r*0.01
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
    param.append(r)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Risk Free Rate')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()


"""

How Correlation between Assets Affect Call Option Price

"""

s1 = 50
s2 = 50
K = 50
t = 0
T = 0.5
sigma1 = 0.3
sigma2 = 0.3
r = 0.05
m = 10**5
price=[]
param=[]
for rho in range(1,100,1):
    rho = rho * 0.01
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'call', True)
    price.append(C.value_with_control_variate()[0])
    param.append(rho)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Rho')
# naming the y axis
plt.ylabel('Call Option Price')
plt.title(title+ ' Call Option')
plt.show()

"""

How Correlation between Assets Affects Put Option Price

"""

s1 = 50
s2 = 50
K = 50
t = 0
T = 0.5
sigma1 = 0.3
sigma2 = 0.3
r = 0.05
m = 10**5
price=[]
param=[]
for rho in range(1,100):
    rho = rho * 0.01
    C = MonteCarloBasketVC(s1, s2, sigma1, sigma2, rho, r, T, K, n, m, 'put', True)
    price.append(C.value_with_control_variate()[0])
    param.append(rho)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Rho')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()
