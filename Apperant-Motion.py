import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a spiral
t = np.linspace(0, 2 * np.pi, 100)
x = t * np.cos(t)
y = t * np.sin(t)

fig, ax = plt.subplots()

# Plot the spiral
line, = ax.plot(x, y)

# Function to rotate the spiral
def update(num):
    # Rotate the points in the x-y plane
    x_rot = x * np.cos(num / 50.0) - y * np.sin(num / 50.0)
    y_rot = x * np.sin(num / 50.0) + y * np.cos(num / 50.0)
    line.set_data(x_rot, y_rot)
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(500), interval=50, blit=True)

plt.show()