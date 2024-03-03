import os
import pygame

from Pieces import King, Queen, Rook, Bishop, Knight, Pawn

board = pygame.image.load(os.path.join("img", "board.png"))
Board = pygame.transform.scale_by(board, 3.8)

SQUARE_W = 86
SQUARE_H = 86


def re_draw_window():
    win.fill("purple")
    win.blit(Board, (board_x, board_y))
    for x in range(8):
        for y in range(8):
            # pygame.draw.rect(win, (255, 0, 0), (board_x+SQUARE_W*x, board_y+SQUARE_H*y, SQUARE_W, SQUARE_H), 1)
            king = Pawn(win, x, y, "w")
            king.draw()
    
    
    pygame.display.update()
    


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

        re_draw_window()
        

        clock.tick(60) 
    pygame.quit()


# pygame setup
pygame.init()
width = 1000
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess game")
clock = pygame.time.Clock()

board_x = (width//2)-Board.get_width()//2
board_y = (height//2)-Board.get_height()//2

print(board_x)
print(board_y)




main()