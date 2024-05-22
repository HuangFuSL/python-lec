import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
x, y = np.random.rand(2, 100)
plt.scatter(x, y, s=3, color='blue', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple scatter plot')
plt.savefig('2-scatter-plot.pgf')
