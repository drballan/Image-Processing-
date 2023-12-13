

import cv2
import numpy as np
from PIL import Image
#Please note that actual camera parameters should be used for accurate depth estimation
# Load the left and right images in grayscale
imgL = cv2.imread('/Users/meltemballan/Downloads/photos_sterio/chair_l.jpg',0)
imgR = cv2.imread('/Users/meltemballan/Downloads/photos_sterio/chair_r.jpg',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
imgL = clahe.apply(imgL)
imgR = clahe.apply(imgR)
print(imgL.shape) #check the image size to inform blocksize
print(imgR.shape)#check the image size to inform blocksize
# Initialize the stereo block matching object

stereo = cv2.StereoBM_create(numDisparities=0, blockSize=9)

# Compute the disparity image
disparity = stereo.compute(imgL,imgR)
# Apply median filter to the disparity map
#disparity = cv2.medianBlur(disparity, 5)
# Normalize the disparity image
#disparity = cv2.normalize(disparity, disparity, alpha=255, beta=0, norm_type=cv2.NORM_MINMAX)
#disparity = np.uint8(disparity)

# Normalize the disparity map to 0-255
min_val, max_val = disparity.min(), disparity.max()
disparity = ((disparity - min_val) / (max_val - min_val) * 255).astype(np.uint8)
# Adjust contrast and brightness
alpha = 3 # Contrast control (1.0-3.0)
beta = 100  # Brightness control (0-100)

disparity = cv2.convertScaleAbs(disparity, alpha=alpha, beta=beta)
# Apply Non-local Means Denoising
disparity = cv2.fastNlMeansDenoising(disparity, None, 10, 7, 21)

# Display the disparity map
cv2.imshow('Disparity', disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Pixel density in pixels per inch
ppi = 416

# Convert PPI to pixels per millimeter (PPMM)
ppmm = ppi / 25.4

# Focal length in millimeters
f_mm = 24.0

# Baseline in centimeters
b_cm = 17.7

# Convert focal length and baseline to pixels
f = f_mm * ppmm
b = b_cm * 10 * ppmm  # Convert baseline to mm before converting to pixels

# Calculate depth map from disparity
depth_map = np.ones(disparity.shape, np.single)
non_zero_disparity_idx = disparity > 0
depth_map[non_zero_disparity_idx] = f * b / disparity[non_zero_disparity_idx]
# Normalize the depth map to the range 0-255
depth_map = cv2.normalize(depth_map, depth_map, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
depth_map = np.uint8(depth_map)
# Apply Non-Local Means Denoising
#depth_map = cv2.fastNlMeansDenoising(depth_map, None, 10, 7, 21)
# Apply adaptive thresholding
#depth_map = cv2.adaptiveThreshold(depth_map, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)


# Find contours
contours, _ = cv2.findContours(depth_map, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Apply colormap
#depth_map = cv2.applyColorMap(depth_map, cv2.COLORMAP_BONE)


# Draw contours
#for contour in contours:
#   cv2.drawContours(depth_map, [contour], -4, (0, 255, 0), 4)

# Display the depth map
cv2.imshow('Depth map', depth_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Convert OpenCV images to PIL images
imgL_pil = Image.fromarray(imgL)
imgR_pil = Image.fromarray(imgR)
disparity_pil = Image.fromarray(disparity)
depth_map_pil = Image.fromarray(depth_map)

# Save the images with 300 DPI
imgL_pil.save('input_left.jpg', dpi=(300, 300))
imgR_pil.save('input_right.jpg', dpi=(300, 300))
disparity_pil.save('disparity.jpg', dpi=(300, 300))
depth_map_pil.save('depth_map.jpg', dpi=(300, 300))