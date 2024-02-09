# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/zoltan-tasi-HYgAmBKC0hk-unsplash.jpg', cv2.IMREAD_GRAYSCALE)


# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (9, 9), 0)

# Apply Laplacian operator
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

# Find zero-crossings
zero_crossings = ((laplacian[:-1, :-1] * laplacian[1:, 1:]) < 0) | ((laplacian[:-1, :-1] * laplacian[1:, :-1]) < 0)

# Create a binary image to visualize the zero-crossings
zero_crossings_image = np.zeros_like(laplacian)
zero_crossings_image[:-1, :-1][zero_crossings] = 255

# Invert the binary image
zero_crossings_image = 255 - zero_crossings_image

# Normalize the Laplacian image to 0-255
laplacian_normalized = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Convert zero_crossings_image to 8-bit 
zero_crossings_image_8bit = cv2.convertScaleAbs(zero_crossings_image)

# Overlay the zero-crossings on the LoG image
overlay = cv2.add(laplacian_normalized, zero_crossings_image_8bit)

# Display the overlay
plt.imshow(overlay, cmap='gray')
plt.title('Overlay of Zero-crossings on LoG Image')
plt.show()