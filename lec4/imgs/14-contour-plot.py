import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.8, 2.5), layout='constrained')
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.exp(-X**2 - Y**2)
CS = plt.contour(X, Y, Z, cmap='viridis')
plt.clabel(CS)
plt.title('Contour Plot')
plt.savefig('14-contour-plot.pgf')
