from mpl_toolkits.mplot3d import Axes3D
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

# Create a sphere
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = 0.5 * np.outer(np.cos(u), np.sin(v))
y_sphere = 0.5 * np.outer(np.sin(u), np.sin(v))
z_sphere = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the sphere
ax.plot_surface(x_sphere + 2, y_sphere - 2, z_sphere, color='r')
ax.plot_surface(x_sphere - 2, y_sphere + 2, z_sphere, color='b')

# Set the view angle
ax.view_init(elev=20, azim=-35)

# Show the plot
plt.show()