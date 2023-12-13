from PIL import ImageGrab
import json
import numpy as np

# ... Existing code for Ames room animation ...

# Define light source position
light_source = np.array([0, 0, 10])

# Function to calculate shadow coordinates
def calculate_shadow_coordinates(object_position, light_source):
    # Calculate vector from object to light source
    vector = light_source - object_position

    # Calculate shadow coordinates as projection of object onto ground plane
    shadow_coordinates = object_position + vector

    # Set z-coordinate of shadow to 0 (assuming ground plane is at z=0)
    shadow_coordinates[2] = 0

    return shadow_coordinates

# Example usage:
object_position = np.array([2, 2, 3])
shadow_coordinates = calculate_shadow_coordinates(object_position, light_source)
print(shadow_coordinates)