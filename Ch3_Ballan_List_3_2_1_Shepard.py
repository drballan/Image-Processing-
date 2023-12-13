import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
# Create a figure and a subplot
fig, ax = plt.subplots()

# Create a 8x8 checkerboard pattern
checkerboard = np.zeros((10, 10))
checkerboard[::2, ::2] = 1
checkerboard[1::2, 1::2] = 1

# Display the checkerboard pattern
ax.imshow(checkerboard, cmap='gray', interpolation='nearest', extent=[-3, 4, -3, 5], alpha=0.2)


# Create a figure and a subplot
#fig, ax = plt.subplots()

# Create the table tops
table1 = patches.Rectangle((-2, 1), 3, 1, angle=0.60, color='gray')
table2 = patches.Rectangle((.5, -2), 3, 1, angle=45.0, color='gray')

# Add the table tops to the plot
ax.add_patch(table1)
ax.add_patch(table2)

# Create the table legs
plt.plot([-2, -2], [1, 0], 'k-',linewidth=2, color='gray')
plt.plot([1, 1], [1, 0], 'k-', linewidth=2,color='gray')
plt.plot([-2, -2.1], [2, 1], 'k-',linewidth=2, color='gray')
plt.plot([1, 1.1], [2, 1], 'k-', linewidth=2,color='gray')
plt.plot([0.5, 0.5], [-2.8, -1.2], 'k-', linewidth=2,color='gray')
plt.plot([-0.2, -0.2], [-2.2, -1.3], 'k-',linewidth=2, color='gray')
plt.plot([2.6, 2.6], [-0.5, .1], 'k-', linewidth=2,color='gray')
# Set the x and y limits
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])

# Remove the axes
ax.axis('off')

# Show the plot
plt.show()