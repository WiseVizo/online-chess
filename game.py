import os
import pygame
from Board import Board


board = pygame.image.load(os.path.join("img", "board.png"))
Board_img = pygame.transform.scale_by(board, 4)

SQUARE_W = 86
SQUARE_H = 86

my_board = Board()
my_board.fill_board()

def on_click(pos):
    """
    its kinda inaccurate if we click on very edge of the square but as long as we stay near center it works :D
    pos: (x, y)
    return: (row, col) in the board
    """
    col = (pos[0] - board_x)//SQUARE_H
    row = (pos[1] - board_y)//SQUARE_H
    return (row, col)

def re_draw_window():
    win.fill("purple")
    win.blit(Board_img, (board_x, board_y))
    my_board.draw_board(win)  
    pygame.display.update()
    


def main():
    global my_board, selected_piece
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = on_click(pos)
                print(row, col)
                if (0<=row<=7) and (0<=col<=7):
                    if my_board.board[row][col]:
                        if selected_piece[0] == 0:
                            selected_piece[0] = (row, col)
                            my_board.board[row][col].selected = True
                        elif selected_piece[0] and not selected_piece[1]:
                            my_board.board[selected_piece[0][0]][selected_piece[0][1]].selected = False
                            selected_piece[1] = (row, col)
                            my_board.board[row][col].selected = True
                        elif selected_piece[0] and selected_piece[1]:
                            my_board.board[selected_piece[1][0]][selected_piece[1][1]].selected = False
                            selected_piece[0] = selected_piece[1]
                            selected_piece[1] = (row, col)
                            my_board.board[row][col].selected = True

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

selected_piece = [0, 0] # it is to keep track of previous selected piece and last ele of the list will be current selected piece

main()