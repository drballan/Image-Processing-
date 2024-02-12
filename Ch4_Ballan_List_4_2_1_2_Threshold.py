import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/wild.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the mean and median pixel values
mean_value = np.mean(image)
median_value = np.median(image)

# Apply global thresholding with mean value
_, thresholded_mean = cv2.threshold(image, mean_value, 255, cv2.THRESH_BINARY)

# Apply global thresholding with median value
_, thresholded_median = cv2.threshold(image, median_value, 255, cv2.THRESH_BINARY)

# Calculate the difference between the mean and median thresholded images
difference = cv2.absdiff(thresholded_mean, thresholded_median)

# Display the images
# Calculate the difference between the mean and median thresholded images
difference = cv2.absdiff(thresholded_mean, thresholded_median)

# Display the images
plt.figure(figsize=(8, 8))  

plt.subplot(2, 2, 1)  
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 2, 2)  
plt.imshow(thresholded_mean, cmap='gray')
plt.title('Mean Thresholded Image')

plt.subplot(2, 2, 3)  
plt.imshow(thresholded_median, cmap='gray')
plt.title('Median Thresholded Image')

plt.subplot(2, 2, 4)  
plt.imshow(difference, cmap='gray')
plt.title('Difference between Mean and Median Images')

plt.tight_layout()  # Add this line to prevent overlap of subplots

# Save the figure before displaying it
plt.savefig('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/comparison_figure.png')
plt.show()
# Save the results
cv2.imwrite('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/originaingray.jpg', image)
cv2.imwrite('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/thresholded_mean.jpg', thresholded_mean)
cv2.imwrite('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/thresholded_median.jpg', thresholded_median)
cv2.imwrite('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/difference.jpg', difference)
