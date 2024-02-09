import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the first image
image_path1 = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/yan-ots-UuBR5kbvt4Y-unsplash.jpg'
image1 = cv2.imread(image_path1)

# Load the second image
image_path2 = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/neom-9uL7tKuVAq0-unsplash.jpg'
image2 = cv2.imread(image_path2)

# Make sure both images are the same size
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# Overlay the two images
overlay = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

# Create a noise image
noise = np.random.normal(0, 1, overlay.shape).astype(np.uint8)

# Add the noise to the overlay
noisy_overlay = cv2.addWeighted(overlay, 0.8, noise, 0.2, 0)
# Save the noisy overlay
output_path = '/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/noisy_overlay.jpg'
cv2.imwrite(output_path, noisy_overlay)
# Display the noisy overlay
plt.figure(figsize=(10, 5))
plt.imshow(cv2.cvtColor(noisy_overlay, cv2.COLOR_BGR2RGB))
plt.title('Noisy Overlay')
plt.show()