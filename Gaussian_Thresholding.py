import cv2
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt

def apply_gaussian_thresholding(image, sigma):
    # Convert the image to floating point for calculations
    image_float = image.astype(float)
    # Scale the image intensities to the 0-255 range
    image_scaled = ((image_float - np.min(image_float)) / (np.max(image_float) - np.min(image_float))) * 255

    # Calculate the Gaussian weights
    weights = np.zeros_like(image_float)
    weights[image_scaled.shape[0]//2, image_scaled.shape[1]//2] = 1
    weights = gaussian_filter(weights, sigma)

    # Calculate the weighted sum of the pixel intensities
    weighted_sum = gaussian_filter(image_scaled, sigma)
    print(f'Max weighted_sum: {np.max(weighted_sum)}, Min weighted_sum: {np.min(weighted_sum)}')

    # Calculate the sum of the weights
    sum_weights = gaussian_filter(weights, sigma)
    print(f'Max sum_weights: {np.max(sum_weights)}, Min sum_weights: {np.min(sum_weights)}')

    # Calculate the threshold for each pixel

    threshold = weighted_sum / (sum_weights + 1e-10)
    print(f"Max threshold: {np.max(threshold)}, Min threshold: {np.min(threshold)}")
    print(f"Max image intensity: {np.max(image_scaled)}, Min image intensity: {np.min(image_scaled)}")
    # Apply the thresholding operation to the original image
    thresholded_image = np.where(image_scaled >= threshold, 255, 0).astype(np.uint8)

    return thresholded_image

# Load the image
image_path = "/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/library-of-congress-t5fqtwIn9HQ-unsplash.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Define a range of sigma values to test
sigma_values = np.linspace(1, 5, 5)

# Split the image into a training set and a validation set
train_image = image[:image.shape[0]//2, :image.shape[1]//2]
valid_image = image[image.shape[0]//2:, image.shape[1]//2:]

# Find the sigma value that gives the best thresholding results on the validation set
best_sigma = None
best_score = float('inf')

for sigma in sigma_values:
    # Apply Gaussian thresholding to the training set
    thresholded_train_image = apply_gaussian_thresholding(train_image, sigma)

    # Apply the same thresholding to the validation set
    thresholded_valid_image = apply_gaussian_thresholding(valid_image, sigma)

    # Calculate the difference between the thresholded validation image and the original validation image
    score = np.sum((valid_image - thresholded_valid_image)**2)

    # Update the best sigma value if the current score is lower
    if score < best_score:
        best_score = score
        best_sigma = sigma

# Apply Gaussian thresholding to the entire image using the best sigma value
thresholded_image = apply_gaussian_thresholding(image, best_sigma)

# Display the images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Optimized Recursive Gaussian-Weighted Thresholded Image')

plt.tight_layout()
plt.show()