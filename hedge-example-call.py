import numpy as np
from matplotlib import pyplot as plt 
from py_vollib.black_scholes  import black_scholes as bs
from py_vollib.black.greeks.analytical import delta

#price of underlying asset
s_present = 100

#possible price of asset after one year
s_future = np.arange(1, 201)

#number of stocks bought
bought_amount = 1000

#total cost
stocks_cost = s_present * bought_amount

plt.plot(s_future, (s_future * bought_amount) - stocks_cost, label = 'No options hedged')

#risk free rate
r = 0.02
#volatility
sigma = 0.4
#time in years
t = 1

#strike price
k = 110
v1 = round(delta('c', s_present, k, t, r, sigma), 3)
bs_present = bs('c', s_present, k, t, r, sigma)
stocks_with_hedge = 1000 * (1 - v1)
options_with_hedge = 1000 * v1
hedge_stocks_cost = s_present * stocks_with_hedge
options_cost = bs_present * options_with_hedge

c = []
for i in range(len(s_future)):
    c.append(((s_future[i] * stocks_with_hedge) - hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * options_with_hedge) - options_cost))
plt.plot(s_future, c, label = 'K = 110')

#strike price
k = 105
v1 = round(delta('c', s_present, k, t, r, sigma), 3)
bs_present = bs('c', s_present, k, t, r, sigma)
stocks_with_hedge = 1000 * (1 - v1)
options_with_hedge = 1000 * v1
hedge_stocks_cost = s_present * stocks_with_hedge
options_cost = bs_present * options_with_hedge

c = []
for i in range(len(s_future)):
    c.append(((s_future[i] * stocks_with_hedge) - hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * options_with_hedge) - options_cost))
plt.plot(s_future, c, label = 'K = 105')

#strike price
k = 100
v1 = round(delta('c', s_present, k, t, r, sigma), 3)
bs_present = bs('c', s_present, k, t, r, sigma)
stocks_with_hedge = 1000 * (1 - v1)
options_with_hedge = 1000 * v1
hedge_stocks_cost = s_present * stocks_with_hedge
options_cost = bs_present * options_with_hedge

c = []
for i in range(len(s_future)):
    c.append(((s_future[i] * stocks_with_hedge) - hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * options_with_hedge) - options_cost))
plt.plot(s_future, c, label = 'K = 100')

#strike price
k = 95
v1 = round(delta('c', s_present, k, t, r, sigma), 3)
bs_present = bs('c', s_present, k, t, r, sigma)
stocks_with_hedge = 1000 * (1 - v1)
options_with_hedge = 1000 * v1
hedge_stocks_cost = s_present * stocks_with_hedge
options_cost = bs_present * options_with_hedge

c = []
for i in range(len(s_future)):
    c.append(((s_future[i] * stocks_with_hedge) - hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * options_with_hedge) - options_cost))
plt.plot(s_future, c, label = 'K = 95')

#strike price
k = 90
v1 = round(delta('c', s_present, k, t, r, sigma), 3)
bs_present = bs('c', s_present, k, t, r, sigma)
stocks_with_hedge = 1000 * (1 - v1)
options_with_hedge = 1000 * v1
hedge_stocks_cost = s_present * stocks_with_hedge
options_cost = bs_present * options_with_hedge

c = []
for i in range(len(s_future)):
    c.append(((s_future[i] * stocks_with_hedge) - hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * options_with_hedge) - options_cost))
plt.plot(s_future, c, label = 'K = 90')


plt.suptitle("Delta hedging 1000 stocks using calls") 
plt.title("S = 100, r = 0.02, t = 1, $\sigma$ = 0.4")
plt.xlabel("Stock Price after 1 year") 
plt.ylabel("Net Profit/Loss") 
plt.legend()
plt.show()