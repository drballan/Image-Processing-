import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Ellipse
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create the figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the checkerboard
X = np.arange(8)
Y = np.arange(8)
X, Y = np.meshgrid(X, Y)
Z = np.zeros((8, 8))
colors = np.empty(X.shape, dtype=str)
for y in range(8):
    for x in range(8):
        if (x + y) % 2 == 0:
            colors[x, y] = 'k'
        else:
            colors[x, y] = 'w'
ax.plot_surface(X, Y, Z, facecolors=colors, shade=False)


# Define the parameters for the cylinder
x = np.linspace(3.5, 5.5, 100)  # Adjust the x coordinates
z = np.linspace(0, 1, 100)
# Define the parameters for the shadow
x_shadow = np.linspace(3, 6, 100)  # Adjust the x coordinates
z_shadow = np.linspace(0, 1, 100)

# Draw multiple concentric cylinders to give the illusion of a shadow
for r in np.linspace(0.01, 1.5, 10):  # Adjust the radius
    Xc_shadow, Zc_shadow = np.meshgrid(x_shadow, z_shadow)
    Yc_shadow = np.sqrt(r**2 - (Xc_shadow - 4.5)**2) + 4.5  # Adjust the center
    ax.plot_surface(Xc_shadow, Yc_shadow, Zc_shadow, color='gray', alpha=0.2)
    ax.plot_surface(Xc_shadow, (2*4.5)-Yc_shadow, Zc_shadow, color='gray', alpha=0.2)

# Define the parameters for the cylinder
x_cylinder = np.linspace(3.5, 5.5, 100)  # Adjust the x coordinates
z_cylinder = np.linspace(0, 1, 100)

# Draw multiple concentric cylinders to give the illusion of a solid object
for r in np.linspace(0.01, 1, 10):  # Adjust the radius
    Xc_cylinder, Zc_cylinder = np.meshgrid(x_cylinder, z_cylinder)
    Yc_cylinder = np.sqrt(r**2 - (Xc_cylinder - 4.5)**2) + 4.5  # Adjust the center
    ax.plot_surface(Xc_cylinder, Yc_cylinder, Zc_cylinder, color='green')
    ax.plot_surface(Xc_cylinder, (2*4.5)-Yc_cylinder, Zc_cylinder, color='green')
# Set the x, y and z limits
ax.set_xlim([0, 8])
ax.set_ylim([0, 8])
ax.set_zlim([0, 1])

# Show the plot
plt.show()