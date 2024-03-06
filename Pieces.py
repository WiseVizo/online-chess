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

board_x = 168
board_y = 28
SQUARE = 86

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
    
    def move(self):
        pass

    def draw(self, screen):
        if self.color == "w":
            self.image = W[self.piece_index]
        else:
            self.image = B[self.piece_index]
        x = board_x + self.column*SQUARE
        y = board_y + self.row*SQUARE
        screen.blit(self.image, (x, y))
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), (x, y, SQUARE, SQUARE), 2)


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
        super().__init__( row, column, color, 5)

        
        
