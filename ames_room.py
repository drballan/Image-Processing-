import numpy as np
import cv2

# Create a checkerboard room
room = np.zeros((200, 200))
room[::2, :] = 1

# Define the perspective transformation matrix
pts1 = np.float32([[50,50],[150,50],[50,150],[150,150]])
pts2 = np.float32([[10,100],[200,50],[10,200],[200,200]])
M = cv2.getPerspectiveTransform(pts1,pts2)

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('ames_room_illusion.mp4', fourcc, 30.0, (200, 200), isColor=False)

for i in range(100):
    # Apply the perspective distortion
    distorted_room = cv2.warpPerspective(room, M, (200, 200))

    # Write the frame to the video file
    out.write(np.uint8(distorted_room * 255))

# Release the VideoWriter
out.release()