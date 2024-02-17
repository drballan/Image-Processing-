import matplotlib.pyplot as plt
from PIL import Image

# Specify the location and the name of the image
image = Image.open("Original Image")

# Convert the image to RGB mode. Some images can already be in RGB format; but, this is a safe step to make sure.
image = image.convert("RGB")

# Define the region of interest (ROI)
roi_left = 1510
roi_right = 1514
roi_top = 2014
roi_bottom = 2018

# Create a new image for the ROI
roi_width = roi_right - roi_left
roi_height = roi_bottom - roi_top
roi_image = Image.new("RGB", (roi_width, roi_height))

roi_rgb_values = []

for x in range(roi_left, roi_right):
    for y in range(roi_top, roi_bottom):
        pixel_color = image.getpixel((x, y))
        roi_image.putpixel((x - roi_left, y - roi_top), pixel_color)
        roi_rgb_values.append((x, y, pixel_color))

# Display the original image, the ROI, and the table side by side
# ...
# Your code here
# ...
plt.show()
