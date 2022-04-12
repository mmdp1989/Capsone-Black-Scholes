import py_vollib
from matplotlib import pyplot as plt 
from py_vollib.black_scholes.implied_volatility import implied_volatility as iv

#Data collected from: https://www.barchart.com/stocks/quotes/MSFT/options?moneyness=inTheMoney&expiration=2022-06-17-m
#Date Collected: 05/19/2021 16:30
#Expiry Date: 06/17/2022 (394 days)

#current price
s0 = 243.12
#option price
v0 = [57.90, 54.33, 51.50, 47.50, 44.05, 41.30, 37.55, 34.60, 31.95, 29.35, 27.13, 24.00, 22.73, 19.75, 19.05, 16.53, 15.30, 13.15, 12.10, 10.60]
#strike price
k0 = [195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290]
#risk free rate
r0 = 0.00
#volatility
sigma0 = []
#time in years
t0 = 394/365

for i in range(len(k0)):
    sigma0.append(iv(v0[i], s0, k0[i], t0, r0, 'c'))

skew1 = plt.figure(1)
plt.plot(k0, sigma0)
plt.title("Volatility Skew of MSFT") 
plt.xlabel("Strike Price") 
plt.ylabel("Implied Volatility") 
    
#Data collected from: https://www.barchart.com/stocks/quotes/AAPL/options?expiration=2021-06-18-m&moneyness=inTheMoney
#Date Collected: 05/19/2021 16:30
#Expiry Date: 06/18/2021 (30 days)

#current price
s1 = 124.69
#option price
v1 = [25.08, 22.63, 20.18, 17.80, 15.45, 13.18, 10.95, 8.88, 6.95, 5.23, 3.75, 1.68, 0.66, 0.26, 0.13, 0.08, 0.05, 0.04, 0.03, 0.03]
#strike price
k1 = [100, 102.50, 105, 107.50, 110, 112.50, 115, 117.50, 120, 122.50, 125.50, 130, 135, 140, 145, 150, 155, 160, 165, 170]
#risk free rate
r1 = 0.00
#volatility
sigma1 = []
#time in years
t1 = 30/365

for i in range(len(k1)):
    sigma1.append(iv(v1[i], s1, k1[i], t1, r1, 'c'))

skew1 = plt.figure(2)
plt.plot(k1, sigma1)
plt.title("Volatility Skew of AAPL")
plt.xlabel("Strike Price") 
plt.ylabel("Implied Volatility") 

plt.show()