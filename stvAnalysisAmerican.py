import os
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from BionomalTreeAmerican import BionomalTreeAmerican
title= 'American'


"""

How Strike Price Affects Call Option Price

"""

s0 = 50
t = 0
T = 0.5
sigma = 0.2
r = 0.01
n = 200
price=[]
param=[]
for K in range(10,100,10):
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
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
n = 200
price=[]
param=[]
for K in range(10,100,10):
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
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
n = 200
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
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

s0 = 50
K = 50
t = 0
sigma = 0.2
r = 0.01
n = 200
price=[]
param=[]
for T in range(1,40,1):
    T = T * 0.2
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
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

s0 = 50
K= 35
T = 0.5
t = 0
r = 0.01
n = 200
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
    param.append(sigma)   
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Call Option price')

s0 = 50
K= 50
t = 0
r = 0.01
n = 200
price=[]
param=[]
price=[]
param=[]
for sigma in range(1,100,1):
    sigma=sigma*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
    param.append(sigma)
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Call Option price')

s0 = 50
K= 60
t = 0
r = 0.01
n = 200
price=[]
param=[]
for sigma in range(1,100,1):
    sigma=sigma*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
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

fig.suptitle(title+ 'Option ')
fig.align_labels()

s0 = 50
K= 60
T = 0.5
t = 0
r = 0.01
n = 200
price=[]
param=[]
for sigma in range(1,100,1):
    sigma = sigma*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
    param.append(sigma)   
ax[0].plot(param,price, label = 'ITM', color='r')
ax[0].set_ylabel('Put Option price')

s0 = 50
K= 50
t = 0
r = 0.01
n = 200
price=[]
param=[]
price=[]
param=[]
for sigma in range(1,100,1):
    sigma=sigma*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
    param.append(sigma)
ax[1].plot(param,price, label = 'ATM', color='b')
ax[1].set_ylabel('Put Option price')

s0 = 50
K= 35
t = 0
r = 0.01
n = 200
price=[]
param=[]
for sigma in range(1,100,1):
    sigma=sigma*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
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
K = 50
t = 0
T = 0.5
sigma = 0.2
n = 200
price=[]
param=[]
for r in range(1,40,1):
    r = r*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
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
K = 50
t = 0
T = 0.5
sigma = 0.2
n = 200
price=[]
param=[]
for r in range(1,40,1):
    r = r*0.01
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
    param.append(r)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Risk Free Rate')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()


"""

How Number of Time Steps in Binomial Tree Affects Call Option Price

"""

s0 = 50
K = 50
t = 0
T = 0.5
sigma = 0.2
r = 0.01
price=[]
param=[]
for n in range(1,100):
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'call')
    price.append(C.american_fast_tree())
    param.append(n)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Time Steps')
# naming the y axis
plt.ylabel('Call Option Price')
plt.title(title+ ' Call Option')
plt.show()

"""

How Number of Time Steps in Binomial Tree Affects Put Option Price

"""

s0 = 50
K = 50
t = 0
T = 0.5
sigma = 0.2
r = 0.01
price=[]
param=[]
for n in range(1,100):
    C = BionomalTreeAmerican(s0, sigma, r, T, K, n, 'put')
    price.append(C.american_fast_tree())
    param.append(n)
plt.plot(param,price)
# naming the x axis
plt.xlabel('Time Steps')
# naming the y axis
plt.ylabel('Put Option Price')
plt.title(title+ ' Put Option')
plt.show()
