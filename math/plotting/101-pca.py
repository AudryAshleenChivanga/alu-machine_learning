#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot of the PCA data
scatter = ax.scatter(
    pca_data[:, 0],  # x-axis data
    pca_data[:, 1],  # y-axis data
    pca_data[:, 2],  # z-axis data
    c=labels,        # Color by labels
    cmap='plasma'    # Color map
)

# Add axis labels and title
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')
ax.set_title('PCA of Iris Dataset')

# Add color bar to show mapping of colors to labels
cbar = plt.colorbar(scatter)
cbar.set_label('Iris Species')

# Show the plot
plt.show()
