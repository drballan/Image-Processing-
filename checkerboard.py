import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid for the x and y coordinates
x = np.linspace(-5, 5, 101)
y = np.linspace(-5, 5, 101)
x, y = np.meshgrid(x, y)

# Create a checkerboard pattern
z = (np.floor(x).astype(int) % 2) ^ (np.floor(y).astype(int) % 2)
z = np.floor(x) % 2 ^ np.floor(y) % 2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='gray', edgecolor='k')

plt.show()