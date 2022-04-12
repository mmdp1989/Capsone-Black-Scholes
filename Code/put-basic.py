import numpy as np
from matplotlib import pyplot as plt 
from py_vollib.black_scholes  import black_scholes as bs

#array of stock prices
s = np.arange(1, 176)
s1 = np.arange(100,176)
#strike price
k = 120
#risk free rate
r = 0.10
#volatility
sigma = 0.4
#time in years
t = 1

e = k - s
plt.plot(s, e, label = 'IV')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t, r, sigma))

plt.plot(s,c)
plt.suptitle("Call Premium vs Stock Price") 
plt.title("K = 120, r = 0.10, t = 1, $\sigma$ = 0.4")
plt.xlabel("Stock Price") 
plt.ylabel("Call Premium") 
plt.legend()
plt.show()
