import pygame
import os
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

# scaling small imgs
b = [b_king, b_queen, b_rook, b_bishop, b_knight, b_pawn]
w = [w_king, w_queen, w_rook, w_bishop, w_knight, w_pawn]

B = []
W = []
for piece in b:
    B.append(pygame.transform.scale(piece, (64, 64)))
for piece in w:
    W.append(pygame.transform.scale(piece, (64, 64)))

board_x = 147
board_y = 7
SQUARE = 88
overlap = 0.8
offset_x = 10
offset_y = 10

class Piece:
    """
    screen: pygame surface
    row: row
    column: column
    color: color
    piece_index: for selecting the img from W, B list 
    """
    def __init__(self, row, column, color, piece_index):
        self.row = row
        self.column = column
        self.color = color
        self.selected = False
        self.image = None
        self.piece_index = piece_index

    def is_selected(self):
        return self.selected
    
    def move(self, screen, board, x, y):
        pass

    def draw(self, screen, board):
        if self.color == "w":
            self.image = W[self.piece_index]
        else:
            self.image = B[self.piece_index]
        x = board_x + self.column*SQUARE + self.column*overlap
        y = board_y + self.row*SQUARE + self.column*overlap
        screen.blit(self.image, (x+ offset_x, y+ offset_y))
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, SQUARE, SQUARE), 2)
            self.move(screen, board, x, y)


class King(Piece):
    def __init__(self,  row, column, color):
        super().__init__( row, column, color, 0)
    
class Queen(Piece):
     def __init__(self,  row, column, color):
        super().__init__( row, column, color, 1)
class Rook(Piece):
     def __init__(self,  row, column, color):
        super().__init__( row, column, color, 2)
class Bishop(Piece):
     def __init__(self,  row, column, color):
        super().__init__( row, column, color, 3)
class Knight(Piece):
     def __init__(self,  row, column, color):
        super().__init__( row, column, color, 4)

class Pawn(Piece):
     def __init__(self, row, column, color):
        self.first_move = True
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 5)

     def move(self, screen, board, x , y):
    
        # show all possible moves for white
        if self.color == "w":
            if self.first_move:
                y = y - SQUARE
                pygame.draw.rect(screen, (0, 255, 0), (x, y, SQUARE, SQUARE))
                y = y - SQUARE
                pygame.draw.rect(screen, (0, 255, 0), (x, y, SQUARE, SQUARE))
            else:
                y = y - SQUARE
                pygame.draw.rect(screen, (0, 255, 0), (x, y, SQUARE, SQUARE))
        

     def possible_moves(self):
        moves = [] # all possible moves (row, col) format
        if self.color == "w":
            if self.first_move:
                moves.append((self.row-1, self.col))
                moves.append((self.row-2, self.col))
            else:
                moves.append((self.row-1, self.col))
        return moves