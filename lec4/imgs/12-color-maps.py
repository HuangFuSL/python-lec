import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.8, 2.5), layout='constrained')
x = np.linspace(0, 10, 100)
y = np.sin(x)
colors = y
plt.scatter(x, y, c=colors, cmap='viridis')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Color Maps')
plt.colorbar()
plt.savefig('12-color-maps.pgf')
