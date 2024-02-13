import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/shubham-dhage-qn6LgQnxXAI-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
image_blur = cv2.GaussianBlur(image, (5, 5), 0)

# Apply adaptive thresholding with Otsu's method
_, image_thresh = cv2.threshold(image_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display the original and thresholded images side by side
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original')

plt.subplot(1, 2, 2)
plt.imshow(image_thresh, cmap='gray')
plt.title('Adaptive Threshold')

plt.show()
