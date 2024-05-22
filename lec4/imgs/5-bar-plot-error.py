import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))
np.random.seed(0)

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
x = ['A', 'B', 'C', 'D']
y = [1, 2, 3, 4]
plt.bar(x, y, color='orange', alpha=0.5)
plt.errorbar(x, y, yerr=np.random.rand(4), fmt='none', color='black', capsize=4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple bar plot with error bars')
plt.savefig('5-bar-plot-error.pgf')
