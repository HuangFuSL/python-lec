import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))
np.random.seed(0)

x = np.stack([np.ones(25), np.random.randn(25)])
beta_true = np.array([1, 2])
y = beta_true @ x + np.random.randn(25)
beta_hat = np.linalg.inv(x @ x.T) @ x @ y

fig, ax = plt.subplots(1, 1, figsize=(2.8, 2.5), layout='constrained')
plt.scatter(x[1], y, color='blue', alpha=0.5, s=7)
plt.plot(x[1], beta_hat @ x, color='red', alpha=0.5)
for i in range(25):
    plt.plot([x[1, i], x[1, i]], [y[i], beta_hat @ x[:, i]], color='gray', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regression Result')
plt.savefig('e-1-regression-result.pgf')
