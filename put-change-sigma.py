import numpy as np
from matplotlib import pyplot as plt 
from py_vollib.black_scholes  import black_scholes as bs

#current price
s = np.arange(1, 176)
s1 = np.arange(100,176)
#strike price
k = 120
#risk free rate
r = 0.10
#volatility
sigma1 = 0.8
sigma2 = 0.6
sigma3 = 0.4
sigma4 = 0.2
#time in years
t = 1

e = k - s
plt.plot(s, e, label = 'IV')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t, r, sigma1))

plt.plot(s,c, label = '$\sigma$ = 0.8')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t, r, sigma2))
    
plt.plot(s,c, label = '$\sigma$ = 0.6')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t, r, sigma3))
    
plt.plot(s,c, label = '$\sigma$ = 0.4')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t, r, sigma4))
    
plt.plot(s,c, label = '$\sigma$ = 0.2')

plt.suptitle("Put Premium vs Stock Price") 
plt.title("K = 120, r = 0.10, t = 1")
plt.xlabel("Stock Price") 
plt.ylabel("Put Premium") 
plt.legend()
plt.show()