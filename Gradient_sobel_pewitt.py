import cv2
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/cdc-DTlYPEq9yMM-unsplash.jpg', cv2.IMREAD_GRAYSCALE)



# Define Sobel operator
sobel_x = np.array([
    [-1, -2, 0, 2, 1],
    [-4, -8, 0, 8, 4],
    [-6,-12, 0,12, 6],
    [-4, -8, 0, 8, 4],
    [-1, -2, 0, 2, 1]
])

sobel_y= np.array([
    [-1, -4, -6, -4, -1],
    [-2, -8,-12, -8, -2],
    [ 0,  0,  0,  0,  0],
    [ 2,  8, 12,  8,  2],
    [ 1,  4,  6,  4,  1]
])

# Define Prewitt operator
prewitt_x = np.array([
    [-1, -1, 0, 1, 1],
    [-1, -1, 0, 1, 1],
    [-1, -1, 0, 1, 1],
    [-1, -1, 0, 1, 1],
    [-1, -1, 0, 1, 1]
])

prewitt_y= np.array([
    [-1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1],
    [ 0,  0,  0,  0,  0],
    [ 1,  1,  1,  1,  1],
    [ 1,  1,  1,  1,  1]
])

# Apply Sobel operator
gradient_x_sobel = signal.convolve2d(image, sobel_x, mode='same', boundary='symm')
gradient_y_sobel = signal.convolve2d(image, sobel_y, mode='same', boundary='symm')

# Apply Prewitt operator
gradient_x_prewitt = signal.convolve2d(image, prewitt_x, mode='same', boundary='symm')
gradient_y_prewitt = signal.convolve2d(image, prewitt_y, mode='same', boundary='symm')

# Calculate gradient magnitude for Sobel
gradient_magnitude_sobel = np.sqrt(gradient_x_sobel**2 + gradient_y_sobel**2)

# Normalize to 8-bit scale (0-255)
gradient_magnitude_sobel = (gradient_magnitude_sobel / np.max(gradient_magnitude_sobel) * 255).astype(np.uint8)

# Calculate gradient magnitude for Prewitt
gradient_magnitude_prewitt = np.sqrt(gradient_x_prewitt**2 + gradient_y_prewitt**2)

# Normalize to 8-bit scale (0-255)
gradient_magnitude_prewitt = (gradient_magnitude_prewitt / np.max(gradient_magnitude_prewitt) * 255).astype(np.uint8)

# Apply adaptive thresholding to the gradient magnitude
_, image_thresh_sobel = cv2.threshold(gradient_magnitude_sobel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, image_thresh_prewitt = cv2.threshold(gradient_magnitude_prewitt, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Display the original and thresholded images side by side
plt.figure(figsize=(20, 10))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(1, 3, 2)
plt.imshow(image_thresh_sobel, cmap='gray')
plt.title('Sobel Gradient Threshold')

plt.subplot(1, 3, 3)
plt.imshow(image_thresh_prewitt, cmap='gray')
plt.title('Prewitt Gradient Threshold')

plt.show()