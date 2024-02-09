# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/ram-kishor-4lWZS0XE1jM-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur
sigma = 1.0
blurred = cv2.GaussianBlur(image, (0, 0), sigma)

# Apply Laplacian operator
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

# Convert Laplacian to 8-bit 
laplacian_8bit = cv2.convertScaleAbs(laplacian)

# Apply bilateral filter to reduce noise while preserving edges
filtered = cv2.bilateralFilter(laplacian_8bit, d=6, sigmaColor=150, sigmaSpace=250)

# Convert the filtered image to binary
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define the structuring element
# In this case, we're using a 5x5 square as the structuring element
structuring_element = np.ones((11, 11), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(binary_image, structuring_element,iterations=3)

# Display the original, binary, and dilated images
plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

plt.subplot(133)
plt.imshow(dilated_image, cmap='gray')
plt.title('Dilated Image')

plt.tight_layout()
plt.show()
