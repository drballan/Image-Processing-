import matplotlib.pyplot as plt
import numpy as np

# Create a new figure and add a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a function to draw a line in 3D
def draw_line(ax, p1, p2):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'k-')

# Draw the main lines of the illusion
draw_line(ax, (0.2, 0.5, 0), (0.8, 0.5, 0))
draw_line(ax, (0.2, 0.7, 0), (0.8, 0.7, 0))

# Draw the fins of the illusion
draw_line(ax, (0.2, 0.5, 0), (0.3, 0.6, 0))
draw_line(ax, (0.2, 0.5, 0), (0.3, 0.4, 0))
draw_line(ax, (0.8, 0.5, 0), (0.7, 0.6, 0))
draw_line(ax, (0.8, 0.5, 0), (0.7, 0.4, 0))

# Fins for the second arrow
draw_line(ax, (0.2, 0.7, 0), (0.1, 0.8, 0))
draw_line(ax, (0.2, 0.7, 0), (0.1, 0.6, 0))
draw_line(ax, (0.8, 0.7, 0), (0.9, 0.8, 0))
draw_line(ax, (0.8, 0.7, 0), (0.9, 0.6, 0))

plt.show()