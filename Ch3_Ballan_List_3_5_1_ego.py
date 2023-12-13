import pygame
import numpy as np

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Define the size and spacing of the squares
square_size = 50
square_spacing = 60

# Create a surface for the square
square = pygame.Surface((square_size, square_size))
square.fill((255, 255, 255))
pygame.draw.rect(square, (0, 0, 0), square.get_rect(), 1)

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the grid of squares
    for i in range(0, screen.get_width(), square_spacing):
        for j in range(0, screen.get_height(), square_spacing):
            # Rotate the square
            rotated_square = pygame.transform.rotate(square, angle)

            # Calculate the position of the rotated square
            pos = (i - rotated_square.get_width() // 2, j - rotated_square.get_height() // 2)

            # Draw the rotated square
            screen.blit(rotated_square, pos)

    # Update the angle
    angle += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

