from PIL import Image

# Open the image with an RGBA channel (make sure it has an alpha channel)
image = Image.open("input.png")

# Create a new image with the desired background color and the same size as the original image
# Here, (255, 255, 255, 0) is fully transparent white

background = Image.new("RGBA", image.size, (255, 255, 255, 0))  

# Composite the foreground image (original image) onto the background image
result = Image.alpha_composite(background, image)

# Save the image with the transparent background
result.save("output.png")
