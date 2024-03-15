import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing Example")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Load an image
image = pygame.image.load(os.path.join("img", "black_king.png"))
image_rect = image.get_rect()

# Create a font object
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)
    
    # Draw a line
    pygame.draw.line(screen, RED, (100, 100), (300, 100), 5)
    
    # Draw a rectangle
    pygame.draw.rect(screen, BLUE, (100, 150, 200, 100))
    
    # Draw a circle
    pygame.draw.circle(screen, RED, (400, 300), 50)
    
    # Draw an image
    screen.blit(image, image_rect)
    
    # Render and draw text
    text_surface = font.render("Hello, Pygame!", True, BLUE)
    screen.blit(text_surface, (100, 400))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
