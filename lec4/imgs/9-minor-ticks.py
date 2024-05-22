import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), marker='x', color='blue', alpha=0.5, markersize=5, markevery=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Minor Ticks')
plt.minorticks_on()
plt.xticks(np.arange(0, 11, 1), minor=True)
plt.xticks(np.arange(0, 11, 2), minor=False)
plt.yticks(np.arange(-1, 1.1, 0.1), minor=True)
plt.yticks(np.arange(-1, 1.1, 0.5), minor=False)
plt.savefig('9-minor-ticks.pgf')
