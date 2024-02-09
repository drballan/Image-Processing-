import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/library-of-congress-t5fqtwIn9HQ-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Gaussian thresholding
_, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Display the filtered image
plt.subplot(1, 2, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('Filtered Image')

plt.show()
