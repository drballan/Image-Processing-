import numpy as np

def save_svg(image_array, path):
    """Saves a NumPy array as an SVG image.

    Args:
        image_array: A NumPy array representing the image.
        path: The path to save the SVG image to.
    """

    # Get image dimensions
    height, width, _ = image_array.shape

    # Create the SVG XML markup
    svg_markup = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

    for y in range(height):
        svg_markup += '<path d="'
        for x in range(width):
            r, g, b = image_array[y, x]
            hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
            svg_markup += f'M{x},{y} '
            svg_markup += f'Q{x + 1},{y} '  # Quadratic Bezier curve
        svg_markup += f'" fill="{hex_color}" />\n'

    svg_markup += '</svg>'

    # Write the SVG markup to the file
    with open(path, 'w') as svg_file:
        svg_file.write(svg_markup)

# Example usage:

# Load the JPEG image as a NumPy array.
image_path = '/path/input.jpeg'
image_array = load_jpg(image_path)

# Take a small array from the image.
small_image_array = image_array[1000:1050, 2000:2050]

# Save the small image array as an SVG image.
svg_path = '/path/output.svg'
save_svg(small_image_array, svg_path)
