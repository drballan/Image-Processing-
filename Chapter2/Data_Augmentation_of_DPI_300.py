from PIL import Image
import random
import os

# Define the input and output directories
input_directory = 'input_images/'
output_directory = 'output_images/'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# List all the input image files in the input directory
input_files = os.listdir(input_directory)

# Define augmentation parameters (you can customize these)
rotation_range = (0, 360)  # Range of rotation angles (degrees)
brightness_factor = (0.5, 2.0)  # Range of brightness factors
contrast_factor = (0.5, 2.0)  # Range of contrast factors
output_dpi = 300  # Desired DPI for output images

# Loop through each input image file
for input_file in input_files:
    # Open the input image using Pillow
    image = Image.open(os.path.join(input_directory, input_file))

    # Perform augmentations
    # 1. Rotate the image randomly within the specified range
    rotation_angle = random.uniform(rotation_range[0], rotation_range[1])
    image = image.rotate(rotation_angle)

    # 2. Adjust brightness randomly
    brightness = random.uniform(brightness_factor[0], brightness_factor[1])
    image = ImageEnhance.Brightness(image).enhance(brightness)

    # 3. Adjust contrast randomly
    contrast = random.uniform(contrast_factor[0], contrast_factor[1])
    image = ImageEnhance.Contrast(image).enhance(contrast)

    # Set the DPI of the output image
    image = image.convert('RGB')
    image.info['dpi'] = (output_dpi, output_dpi)

    # Save the augmented image to the output directory
    output_file = os.path.join(output_directory, input_file)
    image.save(output_file, dpi=(output_dpi, output_dpi))

print("Augmentation complete. Images saved in the output directory.")
