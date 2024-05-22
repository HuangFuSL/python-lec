import os

from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

fig, ax = plt.subplots(1, 1, figsize=(2.5, 2.5), layout='constrained')
x = ['A', 'B', 'C', 'D']
y = [1, 2, 3, 4]
plt.bar(x, y, color='orange', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Simple bar plot')
plt.savefig('4-bar-plot.pgf')
