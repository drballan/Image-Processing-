import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/xiao-cui-3S2FmTt4HKE-unsplash.jpg'
image = cv2.imread(image_path)

# Split the image into its color channels
b, g, r = cv2.split(image)

# Create a CLAHE object (Arguments are optional)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

# Apply CLAHE to each color channel
b_clahe = clahe.apply(b)
g_clahe = clahe.apply(g)
r_clahe = clahe.apply(r)

# Merge the channels back together
balanced_image_clahe = cv2.merge([b_clahe, g_clahe, r_clahe])

# Display the original and balanced images side by side
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(balanced_image_clahe, cv2.COLOR_BGR2RGB))
plt.title('Balanced Image (CLAHE)')
plt.show()