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
sigma = 0.4
#time in years
t1 = 3
t2 = 2
t3 = 1
t4 = 0.5

e = k - s
plt.plot(s, e, label = 'IV')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t1, r, sigma))

plt.plot(s,c, label = 't = 3 years')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t2, r, sigma))
    
plt.plot(s,c, label = 't = 2 years')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t3, r, sigma))
    
plt.plot(s,c, label = 't = 1 year')

c = []
for i in range(len(s)):
    c.append(bs('p', s[i], k, t4, r, sigma))
    
plt.plot(s,c, label = 't = 0.5 years')

plt.suptitle("Put Premium vs Stock Price") 
plt.title("K = 120, r = 0.10, $\sigma$ = 0.4")
plt.xlabel("Stock Price") 
plt.ylabel("Put Premium")
plt.legend() 
plt.show()
