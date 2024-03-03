import os
import pygame



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
board = pygame.image.load(os.path.join("img", "board.png"))

# scaling small imgs
b = [b_king, b_queen, b_rook, b_bishop, b_knight, b_pawn]
w = [w_king, w_queen, w_rook, w_bishop, w_knight, w_pawn]
Board = pygame.transform.scale_by(board, 3.5)

B = []
W = []
for piece in b:
    B.append(pygame.transform.scale2x(piece))
for piece in w:
    W.append(pygame.transform.scale2x(piece))

def re_draw_window():
    pygame.display.update()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        win.fill("purple")
        win.blit(Board, ((width//2)-Board.get_width()//2, (height//2)-Board.get_height()//2))

        re_draw_window()
        

        clock.tick(60) 
    pygame.quit()


# pygame setup
pygame.init()
width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess game")
clock = pygame.time.Clock()

main()