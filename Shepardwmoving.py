import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from IPython.display import HTML



fig, ax = plt.subplots()
# Create the table tops
table1 = patches.Rectangle((-2, 1), 3, 1, angle=0.60, color='gray')
table2 = patches.Rectangle((2.5, 1), 3, 1, angle=90.0, color='gray')

# Add the table tops to the plot
ax.add_patch(table1)
ax.add_patch(table2)

# Create the table legs
# ...

# Create the moving object
moving_object = patches.Rectangle((-2, 1), 3, 1, color='blue')

def animate(i):
    # Update the position of the moving object
    moving_object.set_xy((i * 0.1, 1))

    # Return the updated object
    return moving_object,

# Add the moving object to the plot
ax.add_patch(moving_object)

# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=100, blit=True)
# Convert the animation to HTML and display it
HTML(ani.to_jshtml())
# Save the animation
ani.save('animation.gif', writer='imagemagick')
plt.show()