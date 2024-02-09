import cv2
import numpy as np
import pywt
import matplotlib.pyplot as plt

# Load the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/dan-cristian-padure-1k7vrumRHow-unsplash.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Spatial Filtering (Median Filter)
spatial_filtered = cv2.medianBlur(image, 5)

# Apply adaptive threshold
thresholded_image = cv2.adaptiveThreshold(spatial_filtered, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Wavelet Transform (Noise Reduction with PyWavelets)
coeffs = pywt.wavedec2(thresholded_image, 'haar')
threshold = np.std(coeffs[-1]) / 0.6745
new_coeffs = [coeffs[0]] + [tuple((np.abs(detail) > threshold) * detail for detail in details) for details in coeffs[1:]]

# Apply the inverse wavelet transform
wavelet_filtered = pywt.waverec2(new_coeffs, 'db1')

# Convert wavelet_filtered to uint8
wavelet_filtered = cv2.convertScaleAbs(wavelet_filtered)

# Apply Laplacian filter
laplacian_filtered = cv2.Laplacian(wavelet_filtered , cv2.CV_64F)

# Convert Laplacian filter result back to original image data type
laplacian_filtered = cv2.convertScaleAbs(laplacian_filtered)

# Add original image and Laplacian filter result to get sharpened image
# Adjust the weights as needed
sharpened_image = cv2.addWeighted(wavelet_filtered , 0.5, laplacian_filtered, 1.5, 0)

# Display the images
plt.figure(figsize=(15, 15))

plt.subplot(1, 5, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 5, 2)
plt.imshow(spatial_filtered, cmap='gray')
plt.title('Spatial Filtered Image')

plt.subplot(1, 5, 3)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Thresholded Image')

plt.subplot(1, 5, 4)
plt.imshow(wavelet_filtered, cmap='gray')
plt.title('Wavelet Filtered Image')

# Display the Laplacian filtered image
plt.subplot(1, 5, 5)
plt.imshow(laplacian_filtered, cmap='gray')
plt.title('Laplacian Filtered Image')

plt.show()