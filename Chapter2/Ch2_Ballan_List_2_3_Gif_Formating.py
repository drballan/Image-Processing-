from PIL import Image

def handle_gif(gif_image):
    """Handles and preprocesses a GIF image.

    Args:
        gif_image: A GIF image object.

    Returns:
        A preprocessed GIF image object.
    """

    # Convert the GIF image to RGB format.
    rgb_image = gif_image.convert("RGB")

    # Resize the image to a smaller size.
    resized_image = rgb_image.resize((256, 256))

    # Save the preprocessed image as a new GIF file.
    resized_image.save("output.gif")

    return resized_image

if __name__ == "__main__":
    # Load the GIF image.
    gif_image = Image.open("input.gif")

    # Handle and preprocess the GIF image.
    preprocessed_image = handle_gif(gif_image)

    # Display the preprocessed GIF image.
    preprocessed_image.show()
