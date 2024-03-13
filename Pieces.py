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

def is_valid_move( target, board):
    """
    target: [row, col]
    return: Boolean 
    """
    if (0<=target[0]<=7) and (0<=target[1]<=7):
        #check if target location is empty
        if not board[target[0]][target[1]]:
            return True
    return False

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
        self.col  = column
        self.color = color
        self.selected = False
        self.image = None
        self.piece_index = piece_index

    def is_selected(self):
        return self.selected
    
    def move(self, screen, board, x, y):
        moves = self.possible_moves(board)
        if not moves: return
        for move in moves:
            x = board_x + move[1]*SQUARE + self.col*overlap
            y = board_y + move[0]*SQUARE + self.col*overlap
            pygame.draw.rect(screen, (0, 255, 0), (x, y, SQUARE, SQUARE))

    def possible_moves(self, board):
        pass

    def draw(self, screen, board):
        if self.color == "w":
            self.image = W[self.piece_index]
        else:
            self.image = B[self.piece_index]
        x = board_x + self.col*SQUARE + self.col*overlap
        y = board_y + self.row*SQUARE + self.col*overlap
        screen.blit(self.image, (x+ offset_x, y+ offset_y))
        if self.selected:
            # pygame.draw.rect(screen, (255, 0, 0), (x, y, SQUARE, SQUARE), 2)
            self.move(screen, board, x, y)
    
    

    def __str__(self) -> str:
        if self.color == "w":
            return "white_"+ __class__.__name__
        return "black_"+__class__.__name__

class King(Piece):
    def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 0)
    
class Queen(Piece):
     def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 1)
class Rook(Piece):
     def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 2)
class Bishop(Piece):
     def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 3)
class Knight(Piece):
    def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 4)
    
    def __str__(self) -> str:
        if self.color == "w":
            return "white_"+ __class__.__name__
        return "black_"+__class__.__name__

    def possible_moves(self, board):
        moves = []
        # for white
        if self.color == "w":
            #top
            if is_valid_move([self.row-2, self.col-1], board):
                moves.append((self.row-2, self.col-1))
            if is_valid_move([self.row-2, self.col+1], board):
                moves.append((self.row-2, self.col+1)) 
            #bottom 
            if is_valid_move([self.row+2, self.col-1], board):
                moves.append((self.row+2, self.col-1))
            if is_valid_move([self.row+2, self.col+1], board):
                moves.append((self.row+2, self.col+1)) 
            #left
            if is_valid_move([self.row+1, self.col-2], board):
                moves.append((self.row+1, self.col-2))
            if is_valid_move([self.row-1, self.col-2], board):
                moves.append((self.row-1, self.col-2)) 
            #right
            if is_valid_move([self.row+1, self.col+2], board):
                moves.append((self.row+1, self.col+2))
            if is_valid_move([self.row-1, self.col+2], board):
                moves.append((self.row-1, self.col+2)) 
        if self.color == "b":
            #top
            if is_valid_move([self.row+2, self.col-1], board):
                moves.append((self.row+2, self.col-1))
            if is_valid_move([self.row+2, self.col+1], board):
                moves.append((self.row+2, self.col+1)) 
            #bottom 
            if is_valid_move([self.row-2, self.col-1], board):
                moves.append((self.row-2, self.col-1))
            if is_valid_move([self.row-2, self.col+1], board):
                moves.append((self.row-2, self.col+1)) 
            #left
            if is_valid_move([self.row+1, self.col-2], board):
                moves.append((self.row+1, self.col-2))
            if is_valid_move([self.row-1, self.col-2], board):
                moves.append((self.row-1, self.col-2)) 
            #right
            if is_valid_move([self.row+1, self.col+2], board):
                moves.append((self.row+1, self.col+2))
            if is_valid_move([self.row-1, self.col+2], board):
                moves.append((self.row-1, self.col+2)) 
        return moves



class Pawn(Piece):
     def __init__(self, row, column, color):
        self.first_move = True
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 5)

     def __str__(self) -> str:
        if self.color == "w":
            return "white_"+ __class__.__name__
        return "black_"+__class__.__name__

     def move(self, screen, board, x , y):
        
        moves = self.possible_moves(board)
        if not moves: return
        for move in moves:
            x = board_x + move[1]*SQUARE + self.col*overlap
            y = board_y + move[0]*SQUARE + self.col*overlap
            pygame.draw.rect(screen, (0, 255, 0), (x, y, SQUARE, SQUARE))

     def possible_moves(self, board):
        moves = [] # all possible moves (row, col) format
        if self.color == "w":
            if self.first_move:
                if is_valid_move([self.row-1, self.col], board):
                    moves.append((self.row-1, self.col))
                    if is_valid_move([self.row-2, self.col], board):
                        moves.append((self.row-2, self.col))
                else:
                    print("invalid move")
            else:
                if not board[self.row-1][self.col]:
                    moves.append((self.row-1, self.col))
                else:
                    print("invalid move")

     
        if self.color == "b":
            if self.first_move:
                if not board[self.row+1][self.col]:
                    moves.append((self.row+1, self.col))
                    if not board[self.row+2][self.col]:
                        moves.append((self.row+2, self.col))
                else:
                    print("invalid move")
            else:
                if not board[self.row+1][self.col]:
                    moves.append((self.row+1, self.col))
                else:
                    print("invalid move")
        return moves
     
    