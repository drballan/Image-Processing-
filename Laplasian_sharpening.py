import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/wild.jpg', cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Apply Laplacian filter
laplacian_filtered = cv2.Laplacian(thresh, cv2.CV_64F)

# Convert Laplacian filter result back to original image data type
laplacian_filtered = cv2.convertScaleAbs(laplacian_filtered)

# Add original image and Laplacian filter result to get sharpened image
sharpened_image = cv2.addWeighted(thresh, 1.5, laplacian_filtered, -0.5, 0)

# Display the images
plt.figure(figsize=(15, 10))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 3, 2)
plt.imshow(thresh, cmap='gray')
plt.title('Thresholded Image')

plt.subplot(1, 3, 3)
plt.imshow(sharpened_image, cmap='gray')
plt.title('Sharpened Image')

plt.show()