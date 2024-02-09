import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/tetianakobzeva.jpg'
image = cv2.imread(image_path)
# Print the size of the image
print('Image size:', image.shape)
# Calculate the resolution of the image
resolution = image.shape[0] * image.shape[1]

# Print the resolution of the image
print('Image resolution:', resolution)
# Apply mean filtering
mean_filtered_image = cv2.blur(image, (61, 61))

# Apply median filtering
median_filtered_image = cv2.medianBlur(image, 61)

# Apply Gaussian blurring
gaussian_blurred_image = cv2.GaussianBlur(image, (61, 61), 61/3)

# Display the original and filtered images side by side
plt.figure(figsize=(15, 10))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(mean_filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Mean Filtered Image')
plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(median_filtered_image, cv2.COLOR_BGR2RGB))
plt.title('Median Filtered Image')
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(gaussian_blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Gaussian Blurred Image')
plt.tight_layout()  # Improve layout
plt.show()