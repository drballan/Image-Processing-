import numpy as np
import cv2
import matplotlib.pyplot as plt

# Read the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/susanne-schwarz-ouO7S8j332Y-unsplash.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert the image to the logarithmic domain
log_image = np.log1p(np.array(gray_image, dtype="float"))

# Perform the 2D Fast Fourier Transform to get the frequency transform of the image
f = np.fft.fft2(log_image)
fshift = np.fft.fftshift(f)

# Create a high-pass filter mask
rows, cols = gray_image.shape
crow, ccol = rows // 2, cols // 2 # center of the image
mask = np.ones((rows, cols), np.uint8)
# Define the size of the square and the mask value
square_size = 10
mask_value = 0.5

# Set the square region in the center of the mask to the mask value
mask[crow-square_size:crow+square_size, ccol-square_size:ccol+square_size] = mask_value

# Apply the mask to the frequency transform
fshift_filtered = fshift * mask

# Perform the inverse 2D Fast Fourier Transform to get the filtered image
f_ishift = np.fft.ifftshift(fshift_filtered)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Convert the image back to the original domain by applying the exponential function
img_back = np.expm1(img_back)

# Normalize the image to the range [0, 255]
img_back = cv2.normalize(img_back, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
# Display the original and filtered images side by side
plt.figure(figsize=(15, 10), dpi=100)  # Increase figure size and resolution
plt.subplot(1, 2, 1)  # Adjust subplot layout
plt.imshow(gray_image, cmap='gray', interpolation='bicubic')  # Use bicubic interpolation
plt.title('Original Image')  # Add title
plt.xlabel('x')  # Add x label
plt.ylabel('y')  # Add y label

plt.subplot(1, 2, 2)
plt.imshow(img_back, cmap='gray', interpolation='bicubic')  # Use bicubic interpolation
plt.title('Homomorphic Filtered Image')  # Add title
plt.xlabel('x')  # Add x label
plt.ylabel('y')  # Add y label

plt.tight_layout()  # Improve layout
plt.show()