import pygame
import numpy as np
import os
import glob

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Load the images
image_dir = '/Users/meltemballan/Documents/Image_Processing/images/Ego_Motion_2'
image_paths = glob.glob(os.path.join(image_dir, '*.jpg'))
images = [pygame.transform.scale(pygame.image.load(path), (800, 600)) for path in image_paths]
# Main loop
running = True
image_index = 0
frame_rate = 30 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the current image
    screen.blit(images[image_index], (0, 0))

    # Update the image index, stop at the last image
    if image_index < len(images) - 1:
        image_index += 1
    pygame.display.flip()
    # Decrease the frame rate over time
    frame_rate = max(30, frame_rate - 0.1)  # Don't let the frame rate go below 1
    clock.tick(frame_rate)

pygame.quit()