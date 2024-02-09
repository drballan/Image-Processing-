import numpy as np
from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt
import cv2
def apply_gaussian_thresholding(image, sigma):
    # Convert the image to floating point for calculations
    image_float = image.astype(float)

    # Scale the image intensities to the 0-255 range
    image_scaled = ((image_float - np.min(image_float)) / (np.max(image_float) - np.min(image_float))) * 255

    # Calculate the Gaussian weights
    weights = np.zeros_like(image_scaled)
    weights[image_scaled.shape[0]//2, image_scaled.shape[1]//2] = 1
    weights = gaussian_filter(weights, sigma)

    # Calculate the weighted sum of the pixel intensities
    weighted_sum = gaussian_filter(image_scaled, sigma)

    # Calculate the sum of the weights
    sum_weights = gaussian_filter(weights, sigma)

    # Calculate the threshold for each pixel
    threshold = weighted_sum / (sum_weights + 1e-10)

    # Apply the thresholding operation to the original image
    thresholded_image = np.where(image_scaled >= threshold, 255, 0).astype(np.uint8)
    # Apply adaptive thresholding with a different window size
    window_size = 15  # Change this value to adjust the window size
    adaptive_thresh = cv2.adaptiveThreshold(thresholded_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, window_size, 2)

    return adaptive_thresh

# Load the image
image_path = "/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/wild.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian thresholding
sigma = 1.0
thresholded_image = apply_gaussian_thresholding(image, sigma)



# Display the original, thresholded, contrast enhanced, and sharpened images
plt.figure(figsize=(20, 5))

plt.subplot(1, 4, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 4, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Thresholded Image')



plt.tight_layout()
plt.show()