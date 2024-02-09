import numpy as np
import cv2
import matplotlib.pyplot as plt
# Convert the image to grayscale

image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/valentin-salja-dFCn2XeKP0o-unsplash.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# Perform the 2D Fast Fourier Transform to get the frequency transform of the image
f = np.fft.fft2(gray_image)
fshift = np.fft.fftshift(f)

# Create a low-pass filter mask for blurring
rows, cols = gray_image.shape
crow, ccol = rows // 2, cols // 2
mask_blur = np.zeros((rows, cols), np.uint8)
mask_blur[crow-150:crow+150, ccol-150:ccol+150] = 1

# Apply the mask to the frequency transform
fshift_blurred = fshift * mask_blur

# Create a high-pass filter mask for noise reduction
mask_noise = np.ones((rows, cols), np.uint8)
mask_noise[crow-1:crow+1, ccol-1:ccol+1] = 0

# Apply the mask to the frequency transform
fshift_denoised = fshift_blurred * mask_noise

# Perform the inverse 2D Fast Fourier Transform to get the filtered image
f_ishift = np.fft.ifftshift(fshift_denoised)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Display the original and filtered images side by side
plt.figure(figsize=(15, 10), dpi=100)  # Increase figure size and resolution
plt.subplot(1, 2, 1)  # Adjust subplot layout
plt.imshow(gray_image, cmap='gray', interpolation='bicubic')  # Use bicubic interpolation
plt.title('Original Image')  # Add title
plt.xlabel('x')  # Add x label
plt.ylabel('y')  # Add y label

plt.subplot(1, 2, 2)
plt.imshow(img_back, cmap='gray', interpolation='bicubic')  # Use bicubic interpolation
plt.title('Blurred and Denoised Image')  # Add title
plt.xlabel('x')  # Add x label
plt.ylabel('y')  # Add y label

plt.tight_layout()  # Improve layout
plt.show()