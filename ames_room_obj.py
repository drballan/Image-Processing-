import numpy as np
import cv2

# Create a black room
room = np.zeros((200, 200))

# Define the object
object = np.ones((40, 40))

# Create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('moving_object_illusion.mp4', fourcc, 30.0, (200, 200), isColor=False)

for i in range(100):
    # Clear the room
    room = np.zeros((200, 200))

    # Place the object at a new position
    room[i:i+40, i:i+40] = object

    # Write the frame to the video file
    out.write(np.uint8(room * 255))

# Release the VideoWriter
out.release()