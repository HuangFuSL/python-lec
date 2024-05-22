import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), marker='x', color='blue', alpha=0.5, markersize=5, markevery=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Axis Ticks and Labels')
plt.xticks(np.arange(0, 11, 2))
plt.yticks(np.arange(-1, 1.1, 0.2))
plt.savefig('8-axis-ticks.pgf')
