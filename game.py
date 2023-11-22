# Simple pygame program

# Import and initialize the pygame library
import pygame

# Import pygame.locals for easier access to key coordinates

# Updated to conform to flake8 and black standards

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])

# Run until the user asks to quit
running = True
while running == True:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (500, 500), 300)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()