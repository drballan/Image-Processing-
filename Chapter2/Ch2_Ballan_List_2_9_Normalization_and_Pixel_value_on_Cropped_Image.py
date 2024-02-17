from PIL import Image

# Open the image
image = Image.open("input.jpg")

# Get the width and height of the image
width, height = image.size
#Crop the image to reduce size and remove unwanted areas.
cropped_image = image.crop((0, height/3, width-1, height-1))
width, height = cropped_image.size
# Normalize the pixel values to the range [0, 1]
for x in range(width):
    for y in range(height):
        # Get the pixel value at (x, y)
        r, g, b = cropped_image.getpixel((x, y))

        # Normalize the pixel values to the range [0, 1]
        r /= 255.0
        g /= 255.0
        b /= 255.0

        # Set the normalized pixel values
        cropped_image.putpixel((x, y), (int(r * 0), int(g * 255), int(b * 255)))

# Save the normalized image
cropped_image.save("Nomalized_output.jpg")
