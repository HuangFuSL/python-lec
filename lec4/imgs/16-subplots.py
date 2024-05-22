import os

import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

x = np.linspace(0, 10, 100)
y1, y2 = np.sin(x), np.cos(x)
fig, (a, b) = plt.subplots(2, 1, figsize=(2.8, 2.5), layout='constrained', sharex=True)
a.plot(x, y1, color='blue', alpha=0.5)
a.set_ylabel('y')
a.set_title('sin(x)')
b.plot(x, y2, color='red', alpha=0.5)
b.set_xlabel('x')
b.set_ylabel('y')
b.set_title('cos(x)')
fig.suptitle('Subplots')
plt.savefig('16-subplots.pgf')
