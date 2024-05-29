import os

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import norm

os.chdir(os.path.dirname(__file__))

def plot(pos_loc, std, ax_a, ax_b):
    pos = norm(pos_loc, std)
    neg = norm(10 - pos_loc, std)
    N = 2000
    X = np.concatenate([pos.rvs(N), neg.rvs(N)])
    Y = np.concatenate([np.ones(N), np.zeros(N)]) == 1
    X_range = np.linspace(X.min(), X.max(), 200)

    # Plot PDF function
    Y_max = np.concatenate([pos.pdf(X_range), neg.pdf(X_range)]).max()
    ax_a.plot(X_range, pos.pdf(X_range), color='blue', alpha=0.6, label='Positive')
    ax_a.plot(X_range, neg.pdf(X_range), color='red', alpha=0.6, label='Negative')
    ax_a.text(pos_loc, Y_max / 2, r'$\mu={mu}$'.format(mu=pos_loc), ha='center')
    ax_a.text(10 - pos_loc, Y_max / 2, r'$\mu={mu}$'.format(mu=10 - pos_loc), ha='center')

    # Fill TP, TN, FN, FP
    N_range = np.linspace(X.min(), 5, 100)
    P_range = np.linspace(5, X.max(), 100)
    ax_a.fill_between(N_range, neg.pdf(N_range), pos.pdf(N_range), color='red', alpha=0.3, label='TN')
    ax_a.fill_between(N_range, 0, pos.pdf(N_range), color='#AA0055', alpha=0.3, label='FN')
    ax_a.fill_between(P_range, 0, neg.pdf(P_range), color='#5500AA', alpha=0.3, label='FP')
    ax_a.fill_between(P_range, pos.pdf(P_range), neg.pdf(P_range), color='blue', alpha=0.3, label='TP')

    # Misc
    ax_a.plot([5, 5], [0, 0.1], color='black')
    # ax_a.legend(loc='upper right')
    ax_a.set_xlim(X.min(), X.max())
    ax_a.set_ylim(0, Y_max * 1.2)
    ax_a.set_xlabel('X')
    ax_a.set_ylabel('Probability Density')

    # Calculate TP, TN, FN, FP
    N_threshold = 100
    threshold = np.linspace(X.max(), X.min(), N_threshold)
    pred_Y = np.tile(X.reshape(-1, 1), N_threshold) > threshold
    Y = np.tile(Y.reshape(-1, 1), N_threshold)
    TP = (pred_Y & Y).sum(axis=0)
    TN = (~pred_Y & ~Y).sum(axis=0)
    FN = (~pred_Y & Y).sum(axis=0)
    FP = (pred_Y & ~Y).sum(axis=0)

    x = FP / (FP + TN)
    y = TP / (TP + FN)
    ax_b.plot(x, y, color='blue', alpha=0.6)
    ax_b.fill_between(x, y, 0, color='blue', alpha=0.3)
    auc = np.trapz(y, x)
    ax_b.text(0.55, 0.25, f'AUC={auc:.2f}', ha='center')
    ax_b.set_xlabel('False Positive Rate')
    ax_b.set_ylabel('True Positive Rate')
    ax_b.yaxis.set_label_position('right')

fig, ax = plt.subplot_mosaic([[f'{i}a', f'{i}a', f'{i}b'] for i in range(2)], figsize=(4.167, 2.5), layout='constrained')
prev_a, prev_b = None, None
for i in range(2):
    ax_a, ax_b = ax[f'{i}a'], ax[f'{i}b']
    if prev_a is not None:
        ax_a.sharex(prev_a)
        prev_a.set_xlabel('')
        prev_a.set_ylabel('')
    if prev_b is not None:
        ax_b.sharex(prev_b)
        prev_b.set_xlabel('')
        prev_b.set_ylabel('')
    plot(6 + i, 1, ax_a, ax_b)
    prev_a, prev_b = ax_a, ax_b

plt.savefig('1-auc.pgf')