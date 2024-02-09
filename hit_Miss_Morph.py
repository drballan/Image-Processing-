# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2.ximgproc as ximgproc

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/immo-wegmann-raLWowGMCWw-unsplash.jpg', cv2.IMREAD_GRAYSCALE)
# Calculate the median of the grayscale image



# Apply Gaussian blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (9, 9), 1)

# Apply adaptive thresholding to convert the image to binary
binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Define structuring elements for the noise
structuring_element_noise_horizontal = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]], dtype=np.uint8)

# Define structuring elements for the fingerprint patterns
structuring_element_fingerprint_vertical = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]], dtype=np.uint8)
structuring_element_fingerprint_45 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=np.uint8)
structuring_element_fingerprint_minus_45 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.uint8)

# Apply the hit-and-miss operation with each structuring element
noise_image_horizontal = cv2.morphologyEx(binary_image, cv2.MORPH_HITMISS, structuring_element_noise_horizontal)
fingerprint_image_vertical = cv2.morphologyEx(binary_image, cv2.MORPH_HITMISS, structuring_element_fingerprint_vertical)
fingerprint_image_45 = cv2.morphologyEx(binary_image, cv2.MORPH_HITMISS, structuring_element_fingerprint_45)
fingerprint_image_minus_45 = cv2.morphologyEx(binary_image, cv2.MORPH_HITMISS, structuring_element_fingerprint_minus_45)

# Combine the results
combined_image = cv2.add(fingerprint_image_vertical, fingerprint_image_45)
combined_image = cv2.add(combined_image, fingerprint_image_minus_45)

# Subtract the noise from the combined image
clean_image = cv2.subtract(combined_image, noise_image_horizontal)
# Convert the clean image to 8-bit unsigned integers
clean_image_8u = cv2.normalize(clean_image, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Equalize the histogram of the clean image
clean_image_eq = cv2.equalizeHist(clean_image_8u)

# Apply thinning to the clean image
thinned_image = ximgproc.thinning(clean_image_8u)

# Display the results
plt.figure(figsize=(15, 10))
plt.subplot(141), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(142), plt.imshow(combined_image, cmap='gray'), plt.title('Combined Result')
plt.subplot(143), plt.imshow(clean_image, cmap='gray'), plt.title('Clean Image')
plt.subplot(144), plt.imshow(thinned_image, cmap='gray'), plt.title('Thinned Image')
plt.tight_layout()
plt.show()
