from PIL import Image, ImageDraw

# Define the size of the image and the size of each square
img_size = (800, 800)
square_size = 50

# Create a new image with white background
img = Image.new("RGB", img_size, "white")
draw = ImageDraw.Draw(img)

# Draw the checkerboard pattern
for i in range(0, img_size[0], square_size * 2):
    for j in range(0, img_size[1], square_size * 2):
        draw.rectangle([i, j, i + square_size, j + square_size], fill="black")
        draw.rectangle([i + square_size, j + square_size, i + square_size * 2, j + square_size * 2], fill="black")

# Draw the illusion lines
for j in range(square_size, img_size[1], square_size * 2):
    draw.rectangle([0, j, img_size[0], j + square_size], fill="gray")

img.save("checkerboard_illusion.png")