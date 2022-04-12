import numpy as np
from matplotlib import pyplot as plt 
from py_vollib.black_scholes  import black_scholes as bs
from py_vollib.black.greeks.analytical import delta

#price of underlying asset
s_present = 100

#possible price of asset after one year
s_future = np.arange(1, 201)

#number of stocks bought
bought_amount = 2000

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
k = 105

c_delta = round(delta('c', s_present, k, t, r, sigma), 3)

c_bs_present = bs('p', s_present, k, t, r, sigma)
c_stocks_with_hedge = 1000 * (1 - c_delta)
c_options_with_hedge = 1000 * c_delta
c_hedge_stocks_cost = s_present * c_stocks_with_hedge
c_options_cost = c_bs_present * c_options_with_hedge

p_bs_present = bs('p', s_present, k, t, r, sigma)
p_stocks_with_hedge = 1000 * c_delta
p_options_with_hedge = 1000 * (1 - c_delta)
p_hedge_stocks_cost = s_present * p_stocks_with_hedge
p_options_cost = c_bs_present * p_options_with_hedge

c = []
for i in range(len(s_future)):
    c.append( ((s_future[i] * c_stocks_with_hedge) - c_hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * c_options_with_hedge) - c_options_cost) + 
        ((s_future[i] * p_stocks_with_hedge) - p_hedge_stocks_cost) + ((bs('p', s_future[i], k, t, r, sigma) * p_options_with_hedge) - p_options_cost)
    )
plt.plot(s_future, c, label = 'Call and Put')


c_bs_present = bs('p', s_present, k, t, r, sigma)
c_stocks_with_hedge = 2000 * (1 - c_delta)
c_options_with_hedge = 2000 * c_delta
c_hedge_stocks_cost = s_present * c_stocks_with_hedge
c_options_cost = c_bs_present * c_options_with_hedge

c = []
for i in range(len(s_future)):
    c.append( ((s_future[i] * c_stocks_with_hedge) - c_hedge_stocks_cost) + ((bs('c', s_future[i], k, t, r, sigma) * c_options_with_hedge) - c_options_cost))
plt.plot(s_future, c, label = 'Call only')


p_bs_present = bs('p', s_present, k, t, r, sigma)
p_stocks_with_hedge = 2000 * c_delta
p_options_with_hedge = 2000 * (1 - c_delta)
p_hedge_stocks_cost = s_present * p_stocks_with_hedge
p_options_cost = c_bs_present * p_options_with_hedge

c = []
for i in range(len(s_future)):
    c.append(((s_future[i] * p_stocks_with_hedge) - p_hedge_stocks_cost) + ((bs('p', s_future[i], k, t, r, sigma) * p_options_with_hedge) - p_options_cost) )
plt.plot(s_future, c, label = 'Put only')

plt.suptitle("Delta hedging 2000 stocks using calls and puts") 
plt.title("S = 100, r = 0.02, t = 1, $\sigma$ = 0.4")
plt.xlabel("Stock Price after 1 year") 
plt.ylabel("Net Profit/Loss") 
plt.legend()
plt.show()