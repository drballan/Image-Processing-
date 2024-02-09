import cv2
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

# Read the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/simone-hutsch-eXBqaHUt994-unsplash.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply homomorphic filter
gray_image_log = np.log1p(np.array(gray_image, dtype="float"))
M, N = gray_image_log.shape
sigma = 20
X, Y = np.meshgrid(np.linspace(0, N-1, N), np.linspace(0, M-1, M))
centerX = np.ceil(N/2)
centerY = np.ceil(M/2)
gaussianNumerator = (X - centerX)**2 + (Y - centerY)**2

# Low pass and high pass filters
Hlow = np.exp(-gaussianNumerator / (2*sigma*sigma))
Hhigh = 1 - Hlow

# Apply filters and inverse log
gray_image_filtered = np.real(np.fft.ifft2(np.fft.ifftshift(np.fft.fftshift(np.fft.fft2(gray_image_log))*Hhigh)))
gray_image_filtered = np.expm1(gray_image_filtered)
gray_image_filtered = (gray_image_filtered - np.min(gray_image_filtered)) / (np.max(gray_image_filtered) - np.min(gray_image_filtered))

# Apply Gaussian smoothing
sigma = 10  # This value determines the amount of smoothing, adjust as needed
smoothed_img = scipy.ndimage.gaussian_filter(gray_image_filtered, sigma)

# Apply the Laplacian operator
log_img = scipy.ndimage.laplace(smoothed_img)

# Display the original, smoothed, and LoG images
plt.figure(figsize=(10, 10))

plt.subplot(131)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')

plt.subplot(132)
plt.imshow(smoothed_img, cmap='gray')
plt.title('Smoothed Image')

plt.subplot(133)
plt.imshow(log_img, cmap='gray')
plt.title('LoG Image')

plt.tight_layout()  # Improve layout
plt.show()