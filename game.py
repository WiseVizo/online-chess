import os
import pygame
from Board import Board


board = pygame.image.load(os.path.join("img", "board.png"))
Board_img = pygame.transform.scale_by(board, 3.8)

SQUARE_W = 86
SQUARE_H = 86

my_board = Board()
my_board.fill_board()

def re_draw_window():
    win.fill("purple")
    win.blit(Board_img, (board_x, board_y))

    my_board.draw_board(win)

    
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

board_x = (width//2)-Board_img.get_width()//2
board_y = (height//2)-Board_img.get_height()//2


main()