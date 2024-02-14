import cv2
import numpy as np
import pywt
import matplotlib.pyplot as plt

# Load the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/frank-ching-TOHBDSIQfjo-unsplash.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply adaptive threshold
thresholded_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Spatial Filtering (Median Filter)
spatial_filtered = cv2.medianBlur(thresholded_image, 5)
cv2.imwrite('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/spatial_filtered.png', spatial_filtered)

# Frequency Domain Filtering (Low-pass Filter)
dft = cv2.dft(np.float32(thresholded_image), flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
rows, cols = thresholded_image.shape
crow, ccol = rows // 2 , cols // 2
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
freq_filtered = cv2.idft(f_ishift)
freq_filtered = cv2.magnitude(freq_filtered[:,:,0],freq_filtered[:,:,1])
cv2.imwrite('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/freq_filtered.png', freq_filtered)

# Wavelet Transform (Noise Reduction with PyWavelets)
coeffs = pywt.wavedec2(thresholded_image, 'haar')
threshold = np.std(coeffs[-1]) / 0.6745
new_coeffs = [coeffs[0]] + [tuple((np.abs(detail) > threshold) * detail for detail in details) for details in coeffs[1:]]

# Apply the inverse wavelet transform
wavelet_filtered = pywt.waverec2(new_coeffs, 'haar')

# Display the images
plt.figure(figsize=(8, 8))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.subplot(2, 3, 2)
plt.imshow(thresholded_image, cmap='gray')
plt.title('Thresholded Image')
plt.subplot(2, 3, 3)
plt.imshow(spatial_filtered, cmap='gray')
plt.title('Spatial Filtered Image')

plt.subplot(2, 3, 4)
plt.imshow(freq_filtered, cmap='gray')
plt.title('Frequency Filtered Image')

plt.subplot(2, 3, 5)
plt.imshow(wavelet_filtered, cmap='gray')
plt.title('Wavelet Filtered Image')
# Apply Laplacian filter
laplacian_filtered = cv2.Laplacian(wavelet_filtered, cv2.CV_64F)

# Display the Laplacian filtered image
plt.subplot(2, 3, 6)
plt.imshow(laplacian_filtered, cmap='gray')
plt.title('Laplacian Filtered Image')


plt.show()
