import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/library-of-congress-t5fqtwIn9HQ-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Normalize the image
image = cv2.normalize(image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Calculate the histogram
hist = cv2.calcHist([blurred], [0], None, [256], [0, 256])

# Apply simple global thresholding
_, thresholded = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

# Apply block-based adaptive thresholding
block_size = 11
C = 2
block_thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, C)

# Apply window-based adaptive thresholding (same as block-based in OpenCV)
window_thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, C)

# Display the original image and histograms
plt.figure(figsize=(20, 10))

plt.subplot(2, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')


plt.subplot(2, 4, 2)
plt.imshow(thresholded, cmap='gray')
plt.title('Simple Global\nThresholding')


plt.subplot(2, 4, 3)
plt.imshow(block_thresholded, cmap='gray')
plt.title('Block-Based\nAdaptive Thresholding')


plt.subplot(2, 4, 4)
plt.imshow(window_thresholded, cmap='gray')
plt.title('Window-Based\nAdaptive Thresholding')





plt.subplot(2, 4, 7)
plt.plot(hist)
plt.xlabel('Histogram')
plt.axvline(x=127, color='r', linestyle='dashed', linewidth=2)
# Add annotations
max_value = np.argmax(hist)
plt.annotate('Dominant Intensity Values', xy=(max_value, hist[max_value]), xytext=(max_value+50, hist[max_value]+500), 
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Brightness Distribution', xy=(200, hist[200]), xytext=(200+50, hist[200]+500), 
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.annotate('Contrast', xy=(100, hist[100]), xytext=(100+50, hist[100]+500), 
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()