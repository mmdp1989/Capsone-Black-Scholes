import numpy as np
from matplotlib import pyplot as plt 
from py_vollib.black_scholes  import black_scholes as bs

#current price
s = np.arange(1, 176)
s1 = np.arange(100,176)
#strike price
k1 = 200
k2 = 160
k3 = 120
k4 = 80
#risk free rate
r = 0.10
#volatility
sigma = 0.4
#time in years
t = 1

#e = s1 - k
#plt.plot(s1, e, label = 'IV')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k1, t, r, sigma))

plt.plot(s,c, label = 'K = 200')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k2, t, r, sigma))
    
plt.plot(s,c, label = 'K = 160')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k3, t, r, sigma))
    
plt.plot(s,c, label = 'K = 120')

c = []
for i in range(len(s)):
    c.append(bs('c', s[i], k4, t, r, sigma))
    
plt.plot(s,c, label = 'K = 80')

plt.suptitle("Call Premium vs Stock Price") 
plt.title("r = 0.10, t = 1, $\sigma$ = 0.4")
plt.xlabel("Stock Price") 
plt.ylabel("Call Premium") 
plt.legend()
plt.show()