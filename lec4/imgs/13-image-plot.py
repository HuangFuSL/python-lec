import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.8, 2.5), layout='constrained')
heatmap = np.random.rand(10, 10)
plt.imshow(heatmap, cmap='viridis')
plt.colorbar()
plt.title('Image Plot')
plt.savefig('13-image-plot.pgf')
