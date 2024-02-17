from PIL import Image

def get_dpi(image_path):
    # Open the image using PIL (Python Imaging Library)
    img = Image.open(image_path)
    
    # Retrieve the DPI (dots per inch) information from the image metadata
    dpi = img.info.get("dpi")
    
    if dpi:
        return dpi
    else:
        return "DPI information not found in the image metadata."

# Example usage:

image_path = "your_image.jpg"
resolution_info = get_dpi(image_path)
print(f"The DPI/PPI of the image is: {resolution_info}")
