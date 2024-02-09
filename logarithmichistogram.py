import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/shubham-dhage-qn6LgQnxXAI-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Calculate the histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
# Check for low intensity values
low_intensity_count = np.sum(hist[:50])  # Change the value as per your definition of 'low intensity'
# print(f"The image has {int(low_intensity_count)} low intensity pixels.")

# Check for high intensity values
high_intensity_count = np.sum(hist[200:])  # Change the value as per your definition of 'high intensity'
# print(f"The image has {int(high_intensity_count)} high intensity pixels.")
# Find the peak of the histogram
peak = np.argmax(hist)
# Plot the image
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Plot the histogram
plt.subplot(1, 2, 2)
plt.plot(hist)
plt.title('Histogram')
# Annotate the histogram with the low and high intensity counts
plt.annotate(f'Low intensity count: {int(low_intensity_count)}', xy=(25, max(hist)), xytext=(30, max(hist) - 50))
plt.annotate(f'High intensity count: {int(high_intensity_count)}', xy=(225, 0), xytext=(130, 50))
# Draw the peak value on the image
print(f"Peak (threshold): {peak}")
plt.show()


