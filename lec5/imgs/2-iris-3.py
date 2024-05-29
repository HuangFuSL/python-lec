import os

from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(__file__))
np.random.seed(0)

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

fig, ax = plt.subplots(1, 1, figsize=(2.2, 2), sharex='col', sharey='row', layout='constrained')
pca = PCA(n_components=2)
X = pca.fit_transform(iris.data)
lr = LogisticRegression(max_iter=500)
lr.fit(X, iris.target)
grid = np.meshgrid(
    np.linspace(X[:, 0].min(), X[:, 0].max(), 100),
    np.linspace(X[:, 1].min(), X[:, 1].max(), 100)
)
grid_y = lr.predict(np.c_[grid[0].ravel(), grid[1].ravel()]).reshape(grid[0].shape)
ax.contourf(grid[0], grid[1], grid_y, alpha=0.3)
ax.scatter(X[:, 0], X[:, 1], c=iris.target, alpha=0.9, s=5)
plt.savefig('2-iris-3.pgf')
