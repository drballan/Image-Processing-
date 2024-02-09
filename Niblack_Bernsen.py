import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import filters
from skimage.util import img_as_ubyte
from skimage.morphology import disk
from skimage.filters import rank

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/library-of-congress-t5fqtwIn9HQ-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Gaussian thresholding
_, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Apply Niblack thresholding
threshold_niblack = filters.threshold_niblack(blurred)
binary_niblack = blurred > threshold_niblack

# Apply Bernsen thresholding
radius = 15
selem = disk(radius)

local_otsu = rank.otsu(blurred, selem)
binary_bernsen = blurred >= local_otsu

# Display the original image
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Display the Gaussian thresholded image
plt.subplot(1, 4, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('Gaussian Thresholding')

# Display the Niblack thresholded image
plt.subplot(1, 4, 3)
plt.imshow(binary_niblack, cmap='gray')
plt.title('Niblack Thresholding')

# Display the Bernsen thresholded image
plt.subplot(1, 4, 4)
plt.imshow(binary_bernsen, cmap='gray')
plt.title('Bernsen Thresholding')

plt.show()