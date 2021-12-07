import matplotlib.pyplot as plt

import numpy
from tslearn.datasets import CachedDatasets
from tslearn.barycenters import dtw_barycenter_averaging

def plot_per_class(X, y):
    plt.figure(figsize=(12, 3))
    n_clusters = len(set(y))
    for idx_yi, yi in enumerate(set(y)):
        plt.subplot(1, n_clusters, idx_yi + 1)
        sub_dataset = X[y == yi]
        for xx in sub_dataset:
            plt.plot(xx.ravel(), "k-", alpha=.2)
        barycenter = dtw_barycenter_averaging(sub_dataset, 
                                              init_barycenter=sub_dataset[0])
        plt.plot(barycenter.ravel(), "r-")
        plt.xlim(0, X.shape[1])
        plt.ylim(-4, 4)
        
seed = 0
numpy.random.seed(seed)
X_train, y_train, _0, _1 = CachedDatasets().load_dataset("Trace")
# Keep first 3 classes
X_train = X_train[y_train < 4]
y_train = y_train[y_train < 4]

plot_per_class(X_train, y_train)
plt.tight_layout()
plt.savefig("time_series.svg")
numpy.savetxt("time_series.csv", X_train[:, :, 0], delimiter=";")
