import numpy as np


x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b1 = 0.1
n = 10
alpha = 1e-6

for i in range(10000):
    b1 -= alpha * (2 / n) * np.sum((b1 * x - y) * x)
    if i % 5000 == 0:
        print(f'Iteration {i}: b1 = {b1}')
