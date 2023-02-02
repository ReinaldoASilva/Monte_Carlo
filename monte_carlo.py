import random
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 

# Monte Carlo
capital = 100
bet_size = 1

prob_win = 0.5
prob_loss = (1 - prob_win)

win_reward = 1
loss_reward = -1

fig, ax = plt.subplots(figsize=(16,8))

last_result = []

for j in range(100):
    equity_curve = [capital]
    for i in range(100):
        if prob_loss < random.random():
            equity_curve += [equity_curve[-1] + win_reward * bet_size]
        else:
            equity_curve += [equity_curve[-1] + loss_reward * bet_size]
    last_result +=[equity_curve]
    ax.plot(equity_curve)

np.mean(last_result)

# Martigale


capital = 1000
best_size = 10
best_size_start = 10

prob_win = 0.5
prob_loss = (1 - prob_win)
win_reward = 1
loss_reward = -1

fig, ax = plt.subplots(figsize=(16,8))

bet_size = 10
equity_curve = [capital]
for i in range(10000):
    if prob_loss < random.random():
        equity_curve += [equity_curve[-1] + win_reward * bet_size]
        best_size = best_size_start
    else:
        equity_curve += [equity_curve[-1] + loss_reward * bet_size]
        best_size = best_size * 2
    if equity_curve[-1] <= 0:
        break
    

ax.plot(equity_curve)

