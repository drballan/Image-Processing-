from PIL import Image

image = Image.open("/content/sample_data/CKC_23_ConcreteEngine_PresentationTemplateSlides_V2.1-01.png")

# Resize the image to 224x224 pixels.
resized_image = image.resize((400, 300))

# Convert the image to grayscale.
grayscale_image = resized_image.convert('L')

# Save the grayscale image.
grayscale_image.save("/content/sample_data/CKC_23_ConcreteEngine_PresentationTemplateSlides_400300pxl.png")
