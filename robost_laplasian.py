import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/anirudh-YQYacLW8o2U-unsplash.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(image, (21, 21),21/3)
# Increase brightness
brightened = cv2.add(blurred, 250)
# Apply Laplacian filter
laplacian = cv2.Laplacian(blurred , cv2.CV_64F)

# Normalize the Laplacian image
laplacian = cv2.convertScaleAbs(laplacian)

# Display the images
plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(blurred, cmap='gray')
plt.title('Blurred Image')

plt.subplot(1, 3, 3)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Image')

plt.show()