import os

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

os.chdir(os.path.dirname(__file__))
np.random.seed(0)

x = np.stack([np.ones(25), np.random.randn(25)])
beta_true = np.array([1, 2])
y = beta_true @ x + np.random.randn(25)
beta_hat = np.linalg.inv(x @ x.T) @ x @ y

fig, ax = plt.subplots(1, 1, figsize=(2.8, 2.5), layout='constrained')
residuals = y - beta_hat @ x
norm_res = (residuals - residuals.mean()) / residuals.std()
norm_q = norm.ppf(np.linspace(0, 1, 25))
plt.scatter(norm_q, np.sort(norm_res), color='blue', alpha=0.5)
plt.plot(norm_q, norm_q, color='red', alpha=0.7)
plt.xlabel('Theoretical quantiles')
plt.ylabel('Sample quantiles')
plt.title('QQ Plot')
plt.savefig('e-3-qq-plot.pgf')
