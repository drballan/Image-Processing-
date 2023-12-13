import cv2
import numpy as np

# Create a blank image of size 500x500
image = np.zeros((500, 500, 3), dtype=np.uint8)

# Draw a rectangle in the center of the image
cv2.rectangle(image, (250, 250), (150, 150), (0, 0, 255), 2)

# Add text to the image
cv2.putText(image, "Ames Room", (250, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Display the image
cv2.imshow("Ames Room", image)
cv2.waitKey(0)