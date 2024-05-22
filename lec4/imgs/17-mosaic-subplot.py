import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

x = np.linspace(0, 10, 100)
y1, y2 = np.sin(x), np.cos(x)
y3 = y1 / y2
fig, axes = plt.subplot_mosaic([['a', 'b'], ['c', 'c']], figsize=(2.8, 2.5))
axes['a'].plot(x, y1, color='blue', alpha=0.5)
axes['b'].plot(x, y2, color='red', alpha=0.5)
axes['c'].plot(x, y3, color='green', alpha=0.5)
fig.suptitle('Mosaic Subplot')
plt.savefig('17-mosaic-subplot.pgf')
