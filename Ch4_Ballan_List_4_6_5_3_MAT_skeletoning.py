# Python 2/3 compatibility
from __future__ import print_function
import cv2
from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage import filters

# Load the image
image = cv2.imread('/Users/meltemballan/Documents/Image_Processing/CH4_Ballan/national-cancer-institute-L7en7Lb-Ovc-unsplash.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a threshold to create a binary image
threshold = filters.threshold_otsu(image)
binary_image = image > threshold

# Perform skeletonization
skeleton = skeletonize(binary_image)

# Display the original image and the skeleton
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                         sharex=True, sharey=True)

ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title('Original image')

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].set_title('Skeleton of the image')

plt.tight_layout()
plt.show()
