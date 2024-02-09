import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage.util import img_as_ubyte
from skimage.morphology import disk
from skimage.filters import threshold_local, rank

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/library-of-congress-t5fqtwIn9HQ-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Niblack thresholding
window_size = 15
threshold_niblack = threshold_local(blurred, window_size, method='mean', offset=-0.2)
binary_niblack = blurred > threshold_niblack

# Apply Bernsen thresholding
radius = 15
selem = disk(radius)
local_min = rank.minimum(blurred, selem)
local_max = rank.maximum(blurred, selem)
binary_bernsen = blurred >= (local_min + local_max) / 2

# Apply window-based adaptive thresholding
block_size = 11
C = 2
window_thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)

# Display the original image
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Display the Niblack thresholded image
plt.subplot(1, 4, 2)
plt.imshow(binary_niblack, cmap='gray')
plt.title('Niblack Thresholding')

# Display the Bernsen thresholded image
plt.subplot(1, 4, 3)
plt.imshow(binary_bernsen, cmap='gray')
plt.title('Bernsen Thresholding')

# Display the window-based thresholded image
plt.subplot(1, 4, 4)
plt.imshow(window_thresholded, cmap='gray')
plt.title('Window-Based Adaptive Thresholding')

plt.show()