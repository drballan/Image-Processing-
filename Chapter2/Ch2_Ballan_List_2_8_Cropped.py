import PIL.Image as Image

# Open the image
image = Image.open("input")
width, height=image.size
print(width)
print(height)
# Crop the image to a 100x100 pixel square
cropped_image = image.crop((0, 0, 100, 100))
cropped_image.save("cropped.jpg")
