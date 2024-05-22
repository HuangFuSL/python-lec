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
plt.plot(x[1], beta_hat @ x, color='red', alpha=0.7)
x2 = x.copy()
x2.sort(axis=1)
y_err = x2[1].std() * np.sqrt(1 / x2.shape[1] + (x2[1] - x2[1].mean()) ** 2 / np.sum((x2[1] - x2[1].mean()) ** 2))
plt.fill_between(x2[1], (beta_hat @ x2) - y_err, (beta_hat @ x2) + y_err, color='red', alpha=0.3, interpolate=True)
plt.scatter(x[1], y, color='blue', alpha=0.5, s=7)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regression Result with Error')
plt.savefig('e-2-regression-error.pgf')
