
# Python 2/3 compatibility
from __future__ import print_function
import numpy as np
import cv2
import matplotlib.pyplot as plt
# Read the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/zoltan-tasi-HYgAmBKC0hk-unsplash.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert the image to the logarithmic domain
log_image = np.log1p(np.array(gray_image, dtype="float"))

# Perform the 2D Fast Fourier Transform to get the frequency transform of the image
f = np.fft.fft2(log_image)
fshift = np.fft.fftshift(f)

# Create a Gaussian high-pass filter
M, N = gray_image.shape
sigma =3 # This value controls the cutoff frequency, adjust as needed
[X, Y] = np.meshgrid(np.arange(0, N), np.arange(0, M))
centerX = np.ceil(N / 2)
centerY = np.ceil(M / 2)
gaussianNumerator = (X - centerX)**2 + (Y - centerY)**2
# Low pass and high pass filters
Hlow = np.exp(-gaussianNumerator / (2 * sigma * sigma))
Hhigh = 1 - Hlow

# Apply the high-pass filter to the frequency transform
fshift_filtered = fshift * Hhigh

# Perform the inverse 2D Fast Fourier Transform to get the filtered image
f_ishift = np.fft.ifftshift(fshift_filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Convert the image back to the original domain by applying the exponential function
img_back = np.expm1(img_back)

# Normalize the image to the range [0, 255]
img_back = cv2.normalize(img_back, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Perform Canny edge detection
edges = cv2.Canny(img_back, threshold1=5, threshold2=50)

# Display the original, equalized, and edge detected images
plt.figure(figsize=(10, 10))

plt.subplot(121)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')



plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detected Image')

plt.tight_layout()  # Improve layout
plt.show()
