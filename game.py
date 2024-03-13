import os
import pygame
from Board import Board


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

def is_within_board(row, col):
    """
    return: True/False if given coordinate is within the board
    """
    return (0<=row<=7) and (0<=col<=7)


def match_moves(row, col, moves):
    """
    checks if given row and col are present in moves list 
    row: int
    col: int
    moves: [(row, col), ....]
    return: True or False  
    """
    if not moves: return False
    for move in moves:
        if move[0] == row and move[1] == col:
            return True
    return False

def is_valid_move(target, piece):
    """
    target: [row, col]
    return: Boolean 
    """
    if "Pawn" in str(piece):
        if (0<=target[0]<=7) and (0<=target[1]<=7):
            #check if target location is empty
            if not my_board.board[target[0]][target[1]]:
                return True
        return False
    else:
        if (0<=target[0]<=7) and (0<=target[1]<=7):
        #check if target location is empty
            if not my_board.board[target[0]][target[1]]:
                return True
            else:
                if my_board.board[target[0]][target[1]].color == piece.color:
                    return False
                else:
                    return True
        return False


def change_active_color():
    """
    changes active_color variable bwtween "w" or "b"
    """
    global active_color
    if active_color == "w":
        active_color = "b"
    else:
        active_color = "w"

def main():
    global my_board, current_selected_piece
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = on_click(pos)
                print(row, col)
                if is_within_board(row, col):
                    if my_board.board[row][col]:
                        if my_board.board[row][col].color == active_color:
                            if current_selected_piece[0] == 0:
                                current_selected_piece[0] = (row, col)
                                my_board.board[row][col].selected = True
                            elif current_selected_piece[0] and not current_selected_piece[1]:
                                my_board.board[current_selected_piece[0][0]][current_selected_piece[0][1]].selected = False
                                current_selected_piece[1] = (row, col)
                                my_board.board[row][col].selected = True
                            elif current_selected_piece[0] and current_selected_piece[1]:
                                my_board.board[current_selected_piece[1][0]][current_selected_piece[1][1]].selected = False
                                current_selected_piece[0] = current_selected_piece[1]
                                current_selected_piece[1] = (row, col)
                                my_board.board[row][col].selected = True
                s_piece = my_board.selected_piece()
                if s_piece:
                    moves = s_piece.possible_moves(my_board.board)
                    print(f"moves for [{s_piece}]:  {moves}")

                    if match_moves(row, col, moves):
                        print("in board updatition")

                        if is_valid_move([row, col], s_piece):
                            print(f"valid moves [{s_piece}:{moves}:{row, col}]")
                            #update board
                            my_board.board[s_piece.row][s_piece.col] = 0
                            s_piece.row = row
                            s_piece.col = col
                            my_board.board[row][col] = s_piece
                            # special case for pawns
                            if "Pawn" in str(s_piece):
                                s_piece.first_move = False
                            #reset
                            s_piece.selected = False
                            current_selected_piece = [0, 0]
                            change_active_color()
                            

        re_draw_window()
        clock.tick(40) 
    pygame.quit()

board = pygame.image.load(os.path.join("img", "grey-board.png"))
Board_img = pygame.transform.scale_by(board, 1.18)

SQUARE_W = 88
SQUARE_H = 88

my_board = Board()
my_board.fill_board()

# pygame setup
pygame.init()
width = 1000
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("chess game")
clock = pygame.time.Clock()

board_x = (width//2)-Board_img.get_width()//2
board_y = (height//2)-Board_img.get_height()//2

current_selected_piece = [0, 0] # it is to keep track of previous selected piece and last ele of the list will be current selected piece

#keeping track of which color piece turn it is
active_color = "w"
main()