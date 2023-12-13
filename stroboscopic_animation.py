from PIL import Image
import threading
import time

# Define animation frames
frames = [
    Image.open("frame1.png"),
    Image.open("frame2.png"),
    Image.open("frame3.png"),
    Image.open("frame4.png"),
]

# Set frame rate
frame_rate = 10  # frames per second

# Running flag
running = True

def animate_thread():
    global running
    while running:
        for frame in frames:
            # Show frame
            frame.show()
            # Delay between frames
            time.sleep(1 / frame_rate)

# Start animation thread
thread = threading.Thread(target=animate_thread)
thread.start()

# Keep program running until user input
try:
    while True:
        pass
except KeyboardInterrupt:
    running = False

# Wait for thread to finish
thread.join()

# Close all frames
for frame in frames:
    frame.close()