import cv2
import scipy.ndimage
import matplotlib.pyplot as plt

# Read the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/simone-hutsch-eXBqaHUt994-unsplash.jpg'
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_image = clahe.apply(gray_image)

# Apply Gaussian smoothing
sigma = 50  # This value determines the amount of smoothing, adjust as needed
smoothed_img = scipy.ndimage.gaussian_filter(clahe_image, sigma)

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

plt.show()