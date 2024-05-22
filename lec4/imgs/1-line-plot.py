import os

from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.plot([1, 2, 3, 4], [2, 3, 4, 5], color='red', label='Line 2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple line plot')
plt.savefig('1-line-plot.pgf')