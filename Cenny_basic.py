import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/simone-hutsch-eXBqaHUt994-unsplash.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian smoothing
sigma = 50
gaussian_img = cv2.GaussianBlur(gray_image, (5, 5), sigma)

# Apply Canny edge detection
low_threshold = 25
high_threshold = 75
edges = cv2.Canny(gaussian_img, low_threshold, high_threshold)

# Display the original and edge detected images
plt.figure(figsize=(10, 10))

plt.subplot(121)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')

plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detected Image')

plt.show()