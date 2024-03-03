import os
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

#loading imgs
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))

w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()