import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
x = np.linspace(0, 10, 100)
y = 2 * x
y_pos_err = 3 + 0.5 * np.random.rand(100)
y_neg_err = 2 - 0.2 * np.random.rand(100)
plt.plot(x, y, color='black', alpha=0.5)
plt.fill_between(x, y + y_pos_err, y, color='red', alpha=0.5)
plt.fill_between(x, y, y - y_neg_err, color='green', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Error Range')
plt.savefig('11-error-range.pgf')
