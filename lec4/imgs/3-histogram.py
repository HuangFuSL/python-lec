import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))
np.random.seed(0)

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
data = np.random.randn(1000)
plt.hist(data, bins=30, color='green', alpha=0.5)
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title('Simple histogram')
plt.savefig('3-histogram.pgf')
