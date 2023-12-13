import numpy as np
import cv2 as cv
import json

# Load image
illusion_image = cv.imread("/Users/meltemballan/Documents/Image_Processing/images/The-Muller-Lyer-illusion.png")

# Convert the image to grayscale
gray_illusion_image = cv.cvtColor(illusion_image, cv.COLOR_BGR2GRAY)

# Draw initial lines and arrowheads
line1_start = (100, 100)
line1_end = (300, 100)
line2_start = (100, 200)
line2_end = (300, 200)
arrowhead1_start = (280, 90)
arrowhead1_end = (320, 110)
arrowhead2_start = (280, 190)
arrowhead2_end = (320, 210)

cv.line(gray_illusion_image, line1_start, line1_end, (255, 255, 255), 2)
cv.line(gray_illusion_image, line2_start, line2_end, (255, 255, 255), 2)
cv.line(gray_illusion_image, arrowhead1_start, arrowhead1_end, (255, 255, 255), 2)
cv.line(gray_illusion_image, arrowhead2_start, arrowhead2_end, (255, 255, 255), 2)

# Create a grid overlay
grid_size = 50
for i in range(0, gray_illusion_image.shape[1], grid_size):
    cv.line(gray_illusion_image, (i, 0), (i, gray_illusion_image.shape[0]), color=(255,255,255))
for j in range(0, gray_illusion_image.shape[0], grid_size):
    cv.line(gray_illusion_image, (0, j), (gray_illusion_image.shape[1], j), color=(255,255,255))

# Show the image with grid overlay to the user
cv.imshow('Original', gray_illusion_image)
cv.waitKey(0)

# Ask the user for the start and end points of the lines and arrowheads in relative coordinates
line1_start_rel = tuple(map(float, input("Enter start point of line 1 (x, y): ").split(',')))
line1_end_rel = tuple(map(float, input("Enter end point of line 1 (x, y): ").split(',')))
line2_start_rel = tuple(map(float, input("Enter start point of line 2 (x, y): ").split(',')))
line2_end_rel = tuple(map(float, input("Enter end point of line 2 (x, y): ").split(',')))
arrowhead1_start_rel = tuple(map(float, input("Enter start point of arrowhead 1 (x, y): ").split(',')))
arrowhead1_end_rel = tuple(map(float, input("Enter end point of arrowhead 1 (x, y): ").split(',')))
arrowhead2_start_rel = tuple(map(float, input("Enter start point of arrowhead 2 (x, y): ").split(',')))
arrowhead2_end_rel = tuple(map(float, input("Enter end point of arrowhead 2 (x, y): ").split(',')))

# Convert relative coordinates to pixels
line1_start = (int(line1_start_rel[0] * gray_illusion_image.shape[1]), int(line1_start_rel[1] * gray_illusion_image.shape[0]))
line1_end = (int(line1_end_rel[0] * gray_illusion_image.shape[1]), int(line1_end_rel[1] * gray_illusion_image.shape[0]))
line2_start = (int(line2_start_rel[0] * gray_illusion_image.shape[1]), int(line2_start_rel[1] * gray_illusion_image.shape[0]))
line2_end = (int(line2_end_rel[0] * gray_illusion_image.shape[1]), int(line2_end_rel[1] * gray_illusion_image.shape[0]))
arrowhead1_start = (int(arrowhead1_start_rel[0] * gray_illusion_image.shape[1]), int(arrowhead1_start_rel[1] * gray_illusion_image.shape[0]))
arrowhead1_end = (int(arrowhead1_end_rel[0] * gray_illusion_image.shape[1]), int(arrowhead1_end_rel[1] * gray_illusion_image.shape[0]))
arrowhead2_start = (int(arrowhead2_start_rel[0] * gray_illusion_image.shape[1]), int(arrowhead2_start_rel[1] * gray_illusion_image.shape[0]))
arrowhead2_end = (int(arrowhead2_end_rel[0] * gray_illusion_image.shape[1]), int(arrowhead2_end_rel[1] * gray_illusion_image.shape[0]))
# Redraw the lines and arrowheads based on the user's input
cv.line(gray_illusion_image, line1_start, line1_end, (255, 255, 255), 2)
cv.line(gray_illusion_image, line2_start, line2_end, (255, 255, 255), 2)
cv.line(gray_illusion_image, arrowhead1_start, arrowhead1_end, (255, 255, 255), 2)
cv.line(gray_illusion_image, arrowhead2_start, arrowhead2_end, (255, 255, 255), 2)

# Ask the user for the perceived length of each line
perceived_length_line1 = float(input("Enter perceived length of line 1: ").replace(',', '.'))
perceived_length_line2 = float(input("Enter perceived length of line 2: ").replace(',', '.'))
# Show the perceived image to the user
cv.imshow('Perceived', gray_illusion_image)
cv.waitKey(0)
# Define dictionary to store annotations
annotations = {
    "image_array": gray_illusion_image.tolist(),
    "line1_start": line1_start,
    "line1_end": line1_end,
    "line2_start": line2_start,
    "line2_end": line2_end,
    "arrowhead1_start": arrowhead1_start,
    "arrowhead1_end": arrowhead1_end,
    "arrowhead2_start": arrowhead2_start,
    "arrowhead2_end": arrowhead2_end,
    "perceived_length_line1": perceived_length_line1,
    "perceived_length_line2": perceived_length_line2,
}

# Save annotations to a JSON file
with open("/Users/meltemballan/Documents/Image_Processing/images/muller_lyer_annotations.json", "w") as f:
    json.dump(annotations, f)