# Python 2/3 compatibility
from __future__ import print_function
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/ram-kishor-4lWZS0XE1jM-unsplash.jpg', cv2.IMREAD_GRAYSCALE)
# Convert the filtered image to binary
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Define the structuring element
# In this case, we're using a 11x11 square as the structuring element
structuring_element = np.ones((11, 11), np.uint8)
iter=2
# Apply dilation
dilated_image = cv2.dilate(binary_image, structuring_element,iter)

# Apply erosion
eroded_image = cv2.erode(binary_image, structuring_element,iter)

# Apply dilation to the eroded image, effectively performing an opening operation
opened_image = cv2.dilate(eroded_image, structuring_element, iter)
# Display the original, dilated, and eroded images
# Apply dilation
dilated_image = cv2.dilate(binary_image, structuring_element, iterations=1)

# Apply erosion to the dilated image, effectively performing a closing operation
closed_image = cv2.erode(dilated_image, structuring_element, iterations=1)
plt.figure(figsize=(20, 5))

plt.subplot(151)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

plt.subplot(152)
plt.imshow(dilated_image, cmap='gray')
plt.title('Dilated Image')

plt.subplot(153)
plt.imshow(eroded_image, cmap='gray')
plt.title('Eroded Image')

plt.subplot(154)
plt.imshow(opened_image, cmap='gray')
plt.title('Opened Image')
plt.subplot(155)
plt.imshow(closed_image, cmap='gray')
plt.title('Closed Image')
plt.tight_layout()
plt.show()
