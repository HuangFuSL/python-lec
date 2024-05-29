import os

from sklearn.datasets import load_iris
import pandas as pd
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

fig, ax = plt.subplots(4, 4, figsize=(2.7, 2.5), sharex='col', sharey='row', layout='constrained')
for i in range(4):
    for j in range(4):
        ax[i, j].scatter(
            df.iloc[:, j],
            df.iloc[:, i],
            c=df['target'],
            alpha=0.8, s=5
        )
plt.savefig('2-iris-1.pgf')
