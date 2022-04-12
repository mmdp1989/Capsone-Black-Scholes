import numpy as np
from matplotlib import pyplot as plt 
from py_vollib.black_scholes  import black_scholes as bs

#current price
s = np.arange(1, 176)
s1 = np.arange(100,176)
#strike price
k = 120
#risk free rate
r1 = 0.20
r2 = 0.15
r3 = 0.10
r4 = 0.05
#volatility
sigma = 0.4
#time in years
t = 1

e = s1 - k
plt.plot(s1, e, label = 'IV')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k, t, r1, sigma))

plt.plot(s,c, label = 'r = 0.20')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k, t, r2, sigma))
    
plt.plot(s,c, label = 'r = 0.15')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k, t, r3, sigma))
    
plt.plot(s,c, label = 'r = 0.10')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k, t, r4, sigma))
    
plt.plot(s,c, label = 'r = 0.05')

plt.suptitle("Call Premium vs Stock Price") 
plt.title("K = 120, t = 1, $\sigma$ = 0.4")
plt.xlabel("Stock Price") 
plt.ylabel("Call Premium") 
plt.legend()
plt.show()