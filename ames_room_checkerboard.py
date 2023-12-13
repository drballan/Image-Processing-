import matplotlib.pyplot as plt
import numpy as np

# Create a figure
fig = plt.figure()

# Add a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the x, y, and z coordinates
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.zeros_like(x)

# Create a checkerboard pattern
checkerboard = np.zeros_like(x)
checkerboard[::2, ::2] = 1
checkerboard[1::2, 1::2] = 1

# Plot the checkerboard pattern
ax.plot_surface(x, y, z, facecolors=plt.cm.gray(checkerboard), shade=False)

# Set the view angle
ax.view_init(elev=20, azim=-35)

# Show the plot
plt.show()