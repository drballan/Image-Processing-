import cv2
import numpy as np

# Load the original image
img = cv2.imread('/Users/meltemballan/Downloads/Photos-001 (6)/chair_l.jpg', cv2.IMREAD_GRAYSCALE)

# Create the synthetic stereo pair
imgL = np.roll(img, 10, axis=1)  # shift to right
imgR = np.roll(img, -10, axis=1)  # shift to left

# Save the synthetic stereo pair
cv2.imwrite('/Users/meltemballan/Downloads/Photos-001 (6)/synthetic_chair_left.jpg', imgL)
cv2.imwrite('/Users/meltemballan/Downloads/Photos-001 (6)/synthetic_chair_right.jpg', imgR)