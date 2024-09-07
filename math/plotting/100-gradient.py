#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Generate elevation data
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Create scatter plot
scatter_plot = plt.scatter(x, y, c=z, cmap='terrain')  # Corrected scatter plot function

# General labels
plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')
plt.title('Mountain Elevation')

# Colorbar
cbar = plt.colorbar(scatter_plot)  # Corrected to use the scatter plot object
cbar.set_label('Elevation (m)')  # Corrected colorbar label

# Show the plot
plt.show()
