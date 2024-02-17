from PIL import Image, ImageEnhance, ImageOps, ImageFilter
import os

# Load a compressed JPEG image for data augmentation
input_image_path = "input_image.jpg"
image = Image.open(input_image_path)

# Define the output directory for augmented images
output_directory = "augmented_images"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Data Augmentation Functions
def apply_brightness_contrast(image, brightness_factor, contrast_factor):
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)
    return image

def apply_mirror_flip(image):
    return ImageOps.mirror(image)

def apply_rotate(image, degrees):
    return image.rotate(degrees)

def apply_blur(image, radius):
    return image.filter(ImageFilter.GaussianBlur(radius=radius))

# Augmentation Parameters
augmentation_params = [
    {"name": "original", "brightness": 1.0, "contrast": 1.0, "mirror": False, "rotate": 0, "blur": 0},
    {"name": "brightened", "brightness": 1.5, "contrast": 1.0, "mirror": False, "rotate": 0, "blur": 0},
    {"name": "mirrored", "brightness": 1.0, "contrast": 1.0, "mirror": True, "rotate": 0, "blur": 0},
    {"name": "rotated", "brightness": 1.0, "contrast": 1.0, "mirror": False, "rotate": 45, "blur": 0},
    {"name": "blurred", "brightness": 1.0, "contrast": 1.0, "mirror": False, "rotate": 0, "blur": 2},
]

# Apply data augmentation and save augmented images
for params in augmentation_params:
    augmented_image = apply_brightness_contrast(image.copy(), params["brightness"], params["contrast"])
    
    if params["mirror"]:
        augmented_image = apply_mirror_flip(augmented_image)
    
    if params["rotate"] > 0:
        augmented_image = apply_rotate(augmented_image, params["rotate"])
    
    if params["blur"] > 0:
        augmented_image = apply_blur(augmented_image, params["blur"])
    
    # Save the augmented image with a descriptive filename
    output_filename = f"{params['name']}_{os.path.basename(input_image_path)}"
    output_path = os.path.join(output_directory, output_filename)
    augmented_image.save(output_path)
