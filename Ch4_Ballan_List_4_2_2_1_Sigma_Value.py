import cv2
from matplotlib import pyplot as plt

# Load the image
image_path = "/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/wild.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Gaussian filter with different sigma values
#sigma_values = [0.5, 1, 2, 5, 10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
sigma_values=[0.5, 1, 2, 5]
filtered_images = [cv2.GaussianBlur(image, (0, 0), sigma) for sigma in sigma_values]

# Display the original and filtered images
plt.figure(figsize=(20, 5))

plt.subplot(1, len(sigma_values) + 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

for i, sigma in enumerate(sigma_values):
    plt.subplot(1, len(sigma_values) + 1, i + 2)
    plt.imshow(filtered_images[i], cmap='gray')
    plt.title(f'Filtered Image (sigma={sigma})')

plt.tight_layout()
plt.show()
