import os

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))
np.random.seed(0)

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

fig, ax = plt.subplots(1, 1, figsize=(2.2, 2), sharex='col', sharey='row', layout='constrained')
pca = PCA(n_components=2)
X = pca.fit_transform(iris.data)
ax.scatter(X[:, 0], X[:, 1], c=iris.target, alpha=0.8, s=5)
plt.savefig('2-iris-2.pgf')
