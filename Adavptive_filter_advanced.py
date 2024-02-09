import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters #The skimage module is a part of the scikit-image package. It can be installed using pip install scikit-image.

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/library-of-congress-t5fqtwIn9HQ-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Gaussian thresholding
_, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply block-based adaptive thresholding
block_size = 11
C = 2
block_thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)

# Apply window-based adaptive thresholding (same as block-based in OpenCV)
window_thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)

# Display the original image
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Display the Gaussian thresholded image
plt.subplot(1, 4, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('Gaussian Thresholding')

# Display the block-based thresholded image
plt.subplot(1, 4, 3)
plt.imshow(block_thresholded, cmap='gray')
plt.title('Block-Based Adaptive Thresholding')

# Display the window-based thresholded image
plt.subplot(1, 4, 4)
plt.imshow(window_thresholded, cmap='gray')
plt.title('Window-Based Adaptive Thresholding')

plt.show()