# Import necessary libraries
import numpy as np
import cv2
# Load the left and right images in grayscale
imgL = cv2.imread('/Users/meltemballan/Documents/Image_Processing/images/im0.png',0)
imgR = cv2.imread('/Users/meltemballan/Downloads/Image_Processing/images/im1.png',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
imgL = clahe.apply(imgL)
imgR = clahe.apply(imgR)
# Initialize the stereo block matching object
stereo = cv2.StereoBM_create(numDisparities=0, blockSize=21)

# Compute the disparity image
disparity = stereo.compute(imgL,imgR)
# Apply median filter to the disparity map
disparity = cv2.medianBlur(disparity, 5)
# Function to parse calibration file
def parse_calib_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    params = {}
    for line in lines:
        key, value = line.split('=')
        if key in ['cam0', 'cam1']:
            params[key] = np.array([list(map(float, row.split())) for row in value.strip()[1:-1].split(';')])
        elif key in ['doffs', 'baseline', 'width', 'height', 'ndisp', 'isint', 'vmin', 'vmax']:
            params[key] = int(value) if '.' not in value else float(value)

    return params

# Parse calibration file
calib_params = parse_calib_file('/Users/meltemballan/Documents/Image_Processing/images/calib.txt')

# Calculate depth map from disparity
f = calib_params['cam0'][0, 0]  # focal length
b = calib_params['baseline']  # baseline
depth_map = np.ones(disparity.shape, np.single)
non_zero_disparity_idx = disparity > 0
depth_map[non_zero_disparity_idx] = f * b / disparity[non_zero_disparity_idx]

# Normalize the depth map to the range 0-255
depth_map = cv2.normalize(depth_map, depth_map, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
depth_map = np.uint8(depth_map)

# Apply adaptive thresholding
depth_map = cv2.adaptiveThreshold(depth_map, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Find contours
contours, _ = cv2.findContours(depth_map, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours
for contour in contours:
   cv2.drawContours(depth_map, [contour], -4, (0, 255, 0), 4)

# Display the depth map
cv2.imshow('Depth map', depth_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
