# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/zoltan-tasi-HYgAmBKC0hk-unsplash.jpg', cv2.IMREAD_GRAYSCALE)
# Apply Gaussian Blur
sigma = 1.0
blurred = cv2.GaussianBlur(image, (0, 0), sigma)

# Apply Laplacian operator
laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

# Convert Laplacian to 8-bit 
laplacian_8bit = cv2.convertScaleAbs(laplacian)


# Apply bilateral filter to reduce noise while preserving edges
filtered = cv2.bilateralFilter(laplacian_8bit, d=6, sigmaColor=150, sigmaSpace=250)
# Apply Non-Local Means Denoising
#filtered = cv2.fastNlMeansDenoising(filtered, h=100, templateWindowSize=7, searchWindowSize=21)

# Display the result
plt.figure(figsize=(10, 10))

plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')



plt.subplot(122)
plt.imshow(filtered , cmap='gray')
plt.title('LoG Image')

plt.tight_layout()  # Improve layout
plt.show()