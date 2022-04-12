#Code modified from https://blog.quantinsti.com/heston-model/

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime 
import random
from math import sqrt, exp

random.seed(datetime.now())

N = 365          # Number of small sub-steps (time)
n = 100000       # Number of Monte carlo paths
S_0 = np.arange(1, 176)       # Initial stock price
K = 120          # Strike price 
V_0 = 0.09      # Initial variance is square of volatility
kappa = 2       # kappa mean reversion speed
theta = 0.01    # Long-run variance
epsilon = 0.3   # volatility of volatility
rho = 0.0       # correlation 
T1 = 3          # time to maturity
T2 = 2          # time to maturity
T3 = 1          # time to maturity
T4 = 0.5        # time to maturity

S_1 = np.arange(100,176)
e = S_1 - K
plt.plot(S_1, e, label = 'IV')

option_price = []
dt = T1/N        # No. of Time step
for i in range(len(S_0)):
    # Integrate equations: Euler method, Montecarlo vectorized
    V_t = np.ones(n) * V_0
    S_t = np.ones(n) * S_0[i]

    # Generate Montecarlo paths
    for t in range(1,N):  
      # Random numbers for S_t and V_t 
      Z_s = np.random.normal(size=n) 
      Z_v = rho * Z_s + np.sqrt(1 - rho**2) * np.random.normal(size=n) 

      # Euler integration
      V_t = np.maximum(V_t, 0)
      S_t = S_t * np.exp( np.sqrt(V_t * dt) * Z_s - V_t * dt / 2)                     # Stock price process
      V_t = V_t + kappa * (theta - V_t) * dt + epsilon * np.sqrt(V_t * dt) * Z_v      # Volatility process

    option_price.append(np.mean(np.maximum(S_t - K, 0)))
plt.plot(S_0,option_price, label = 't = 3 years')

option_price = []
dt = T2/N        # No. of Time step
for i in range(len(S_0)):
    # Integrate equations: Euler method, Montecarlo vectorized
    V_t = np.ones(n) * V_0
    S_t = np.ones(n) * S_0[i]

    # Generate Montecarlo paths
    for t in range(1,N):  
      # Random numbers for S_t and V_t 
      Z_s = np.random.normal(size=n) 
      Z_v = rho * Z_s + np.sqrt(1 - rho**2) * np.random.normal(size=n) 

      # Euler integration
      V_t = np.maximum(V_t, 0)
      S_t = S_t * np.exp( np.sqrt(V_t * dt) * Z_s - V_t * dt / 2)                     # Stock price process
      V_t = V_t + kappa * (theta - V_t) * dt + epsilon * np.sqrt(V_t * dt) * Z_v      # Volatility process

    option_price.append(np.mean(np.maximum(S_t - K, 0)))
plt.plot(S_0,option_price, label = 't = 2 years')

option_price = []
dt = T3/N        # No. of Time step
for i in range(len(S_0)):
    # Integrate equations: Euler method, Montecarlo vectorized
    V_t = np.ones(n) * V_0
    S_t = np.ones(n) * S_0[i]

    # Generate Montecarlo paths
    for t in range(1,N):  
      # Random numbers for S_t and V_t 
      Z_s = np.random.normal(size=n) 
      Z_v = rho * Z_s + np.sqrt(1 - rho**2) * np.random.normal(size=n) 

      # Euler integration
      V_t = np.maximum(V_t, 0)
      S_t = S_t * np.exp( np.sqrt(V_t * dt) * Z_s - V_t * dt / 2)                     # Stock price process
      V_t = V_t + kappa * (theta - V_t) * dt + epsilon * np.sqrt(V_t * dt) * Z_v      # Volatility process

    option_price.append(np.mean(np.maximum(S_t - K, 0)))
plt.plot(S_0,option_price, label = 't = 1 year')

option_price = []
dt = T4/N        # No. of Time step
for i in range(len(S_0)):
    # Integrate equations: Euler method, Montecarlo vectorized
    V_t = np.ones(n) * V_0
    S_t = np.ones(n) * S_0[i]

    # Generate Montecarlo paths
    for t in range(1,N):  
      # Random numbers for S_t and V_t 
      Z_s = np.random.normal(size=n) 
      Z_v = rho * Z_s + np.sqrt(1 - rho**2) * np.random.normal(size=n) 

      # Euler integration
      V_t = np.maximum(V_t, 0)
      S_t = S_t * np.exp( np.sqrt(V_t * dt) * Z_s - V_t * dt / 2)                     # Stock price process
      V_t = V_t + kappa * (theta - V_t) * dt + epsilon * np.sqrt(V_t * dt) * Z_v      # Volatility process

    option_price.append(np.mean(np.maximum(S_t - K, 0)))
plt.plot(S_0,option_price, label = 't = 0.5 years')

plt.suptitle("No. of paths = 100000, Init variance = 0.09, K = 120, dt = 1/365")
plt.title(r"$\kappa$ = 2, $\rho$ = 0, $\theta$ = 0.01, $\epsilon$ = 0.3") 
plt.xlabel("Stock Price") 
plt.ylabel("Call Premium") 
plt.legend()
plt.show()
