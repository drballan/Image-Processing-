import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/xiao-cui-3S2FmTt4HKE-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Apply histogram equalization
image_eq = cv2.equalizeHist(image)

# Apply contrast stretching
image_stretch = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Display the original, equalized, and stretched images
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.subplot(1, 3, 2)
plt.imshow(image_eq, cmap='gray')
plt.title('Histogram Equalization')
plt.subplot(1, 3, 3)
plt.imshow(image_stretch, cmap='gray')
plt.title('Contrast Stretching')
plt.show()
