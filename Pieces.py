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

def is_king_safe(target: list[tuple], board: list[list], color)->bool:
    """
    tells if king will be safe in target position
    target: [row, col]
    color: kings color 
    return: bool 
    """
    #for white king
    if color == "w":
        #get all black pieces
        for row in range(8):
            for col in range(8):
                if board[row][col]:
                    #if piece exist
                    if board[row][col].color == "b":
                        print("out")
                        if "Pawn" in str(board[row][col]):
                            print("in")
                            moves = board[row][col].possible_moves(board)
                            if match_moves(target[0], target[1], moves):
                                if target[1] == col:
                                    return True
                                else:
                                    return False
                                
                        else:
                            moves = board[row][col].possible_moves(board)
                            if match_moves(target[0], target[1], moves):
                                return False

        return True
    
    # #for black king
    # if color == "b":
    #     #get all white pieces
    #     for row in range(8):
    #         for col in range(8):
    #             if board[row][col]:
    #                 #if piece exist
    #                 if board[row][col].color == "w":
    #                     if "Pawn" in str(board[row][col]):
    #                         moves = board[row][col].possible_moves(board)
    #                         if match_moves(target[0], target[1], moves):
    #                             if target[1] == col:
    #                                 return True
    #                             else:
    #                                 return False
    #                     else:
    #                         moves = board[row][col].possible_moves(board)
    #                         if match_moves(target[0], target[1], moves):
    #                             return False

    #     return True
    
def is_valid_move_pawn( target, board, color):
    """
    target: [row, col]
    color: color of the current piece
    return: Boolean 
    """
    if (0<=target[0]<=7) and (0<=target[1]<=7):
        #check if target location is empty
        if not board[target[0]][target[1]]:
            return True
        else:
            return False

    return False

def is_valid_move_king(target: list[tuple], board: list[list], color)->bool:
    if (0<=target[0]<=7) and (0<=target[1]<=7):
        if is_king_safe(target, board, color):
            return is_valid_move(target, board, color)
    return False

def is_valid_move(target: list, board: list, color:str)->bool:
    """
    will tell if it is a valid move for all the other pieces except pawns and kings
    target: [row, col]
    board:  a 2d list of board 
    color: color of the current piece
    """
    if (0<=target[0]<=7) and (0<=target[1]<=7):
        #check if target location is empty
        if not board[target[0]][target[1]]:
            return True
        else:
            if board[target[0]][target[1]].color == color:
                return False
            else:
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
    
    def move(self, screen, board, x, y, moves):
        # moves = self.possible_moves(board)
        if not moves: return
        for move in moves:
            x = board_x + move[1]*SQUARE + self.col*overlap
            y = board_y + move[0]*SQUARE + self.col*overlap
            # pygame.draw.rect(screen, (0, 255, 0), (x, y, SQUARE, SQUARE))
            pygame.draw.circle(screen, (255, 0, 0), (x+SQUARE*0.5, y+SQUARE*0.5), 40, 5)

    def possible_moves(self, board):
        pass

    def draw(self, screen, board, moves):
        if self.color == "w":
            self.image = W[self.piece_index]
        else:
            self.image = B[self.piece_index]
        x = board_x + self.col*SQUARE + self.col*overlap
        y = board_y + self.row*SQUARE + self.col*overlap
        screen.blit(self.image, (x+ offset_x, y+ offset_y))
        if self.selected:
            # pygame.draw.rect(screen, (255, 0, 0), (x, y, SQUARE, SQUARE), 2)
            self.move(screen, board, x, y, moves)
    
    

    def __str__(self) -> str:
        if self.color == "w":
            return "white_"+ __class__.__name__
        return "black_"+__class__.__name__

count = 0

class King(Piece):
    def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 0)
    
    def possible_moves(self, board):
        global count
        count+=1
        print(f"count: {count}")
        moves = []
        #white
        if self.color == "w":
            #top-right
            if is_valid_move_king([self.row-1, self.col+1], board, self.color):
                moves.append((self.row-1, self.col+1))
            #top
            if is_valid_move_king([self.row-1, self.col], board, self.color):
                moves.append((self.row-1, self.col))
            #top-left
            if is_valid_move_king([self.row-1, self.col-1], board, self.color):
                moves.append((self.row-1, self.col-1))
            #bottom-left
            if is_valid_move_king([self.row+1, self.col-1], board, self.color):
                moves.append((self.row+1, self.col-1))
            #bottom
            if is_valid_move_king([self.row+1, self.col], board, self.color):
                moves.append((self.row+1, self.col))
            #bottom-right
            if is_valid_move_king([self.row+1, self.col+1], board, self.color):
                moves.append((self.row+1, self.col+1))
            #right
            if is_valid_move_king([self.row, self.col+1], board, self.color):
                moves.append((self.row, self.col+1))
            #left
            if is_valid_move_king([self.row, self.col-1], board, self.color):
                moves.append((self.row, self.col-1))
        #black
        if self.color == "b":
            #top-right
            if is_valid_move_king([self.row-1, self.col+1], board, self.color):
                moves.append((self.row-1, self.col+1))
            #top
            if is_valid_move_king([self.row-1, self.col], board, self.color):
                moves.append((self.row-1, self.col))
            #top-left
            if is_valid_move_king([self.row-1, self.col-1], board, self.color):
                moves.append((self.row-1, self.col-1))
            #bottom-left
            if is_valid_move_king([self.row+1, self.col-1], board, self.color):
                moves.append((self.row+1, self.col-1))
            #bottom
            if is_valid_move_king([self.row+1, self.col], board, self.color):
                moves.append((self.row+1, self.col))
            #bottom-right
            if is_valid_move_king([self.row+1, self.col+1], board, self.color):
                moves.append((self.row+1, self.col+1))
            #right
            if is_valid_move_king([self.row, self.col+1], board, self.color):
                moves.append((self.row, self.col+1))
            #left
            if is_valid_move_king([self.row, self.col-1], board, self.color):
                moves.append((self.row, self.col-1))

        return moves
    
    def __str__(self) -> str:
        if self.color == "w":
            return "white_"+ __class__.__name__
        return "black_"+__class__.__name__

    
class Queen(Piece):
     def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 1)
    
     def possible_moves(self, board):
        moves = []
        #white
        if self.color == "w":
             #top-left
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col-i], board, self.color):
                    moves.append((self.row-i, self.col-i))
                    if board[self.row-i][self.col-i]:
                        # piece exist
                        if board[self.row-i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #top
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col], board, self.color):
                    moves.append((self.row-i, self.col))
                    if board[self.row-i][self.col]:
                        # piece exist
                        if board[self.row-i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #top-right
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col+i], board, self.color):
                    moves.append((self.row-i, self.col+i))
                    if board[self.row-i][self.col+i]:
                        # piece exist
                        if board[self.row-i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-left
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col-i], board, self.color):
                    moves.append((self.row+i, self.col-i))
                    if board[self.row+i][self.col-i]:
                        # piece exist
                        if board[self.row+i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col], board, self.color):
                    moves.append((self.row+i, self.col))
                    if board[self.row+i][self.col]:
                        # piece exist
                        if board[self.row+i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-right
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col+i], board, self.color):
                    moves.append((self.row+i, self.col+i))
                    if board[self.row+i][self.col+i]:
                        # piece exist
                        if board[self.row+i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #left
            i = 1
            while True:
                if is_valid_move([self.row, self.col-i], board, self.color):
                    moves.append((self.row, self.col-i))
                    if board[self.row][self.col-i]:
                        # piece exist
                        if board[self.row][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #right
            i = 1
            while True:
                if is_valid_move([self.row, self.col+i], board, self.color):
                    moves.append((self.row, self.col+i))
                    if board[self.row][self.col+i]:
                        # piece exist
                        if board[self.row][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
        #black
        if self.color == "b":
             #top-left
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col-i], board, self.color):
                    moves.append((self.row-i, self.col-i))
                    if board[self.row-i][self.col-i]:
                        # piece exist
                        if board[self.row-i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #top
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col], board, self.color):
                    moves.append((self.row-i, self.col))
                    if board[self.row-i][self.col]:
                        # piece exist
                        if board[self.row-i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #top-right
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col+i], board, self.color):
                    moves.append((self.row-i, self.col+i))
                    if board[self.row-i][self.col+i]:
                        # piece exist
                        if board[self.row-i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-left
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col-i], board, self.color):
                    moves.append((self.row+i, self.col-i))
                    if board[self.row+i][self.col-i]:
                        # piece exist
                        if board[self.row+i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col], board, self.color):
                    moves.append((self.row+i, self.col))
                    if board[self.row+i][self.col]:
                        # piece exist
                        if board[self.row+i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-right
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col+i], board, self.color):
                    moves.append((self.row+i, self.col+i))
                    if board[self.row+i][self.col+i]:
                        # piece exist
                        if board[self.row+i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #left
            i = 1
            while True:
                if is_valid_move([self.row, self.col-i], board, self.color):
                    moves.append((self.row, self.col-i))
                    if board[self.row][self.col-i]:
                        # piece exist
                        if board[self.row][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #right
            i = 1
            while True:
                if is_valid_move([self.row, self.col+i], board, self.color):
                    moves.append((self.row, self.col+i))
                    if board[self.row][self.col+i]:
                        # piece exist
                        if board[self.row][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
        return moves

class Rook(Piece):
     def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 2)

     def possible_moves(self, board):
        moves = []
        #for white
        if self.color == "w":
            #top
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col], board, self.color):
                    moves.append((self.row-i, self.col))
                    if board[self.row-i][self.col]:
                        # piece exist
                        if board[self.row-i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col], board, self.color):
                    moves.append((self.row+i, self.col))
                    if board[self.row+i][self.col]:
                        # piece exist
                        if board[self.row+i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #left
            i = 1
            while True:
                if is_valid_move([self.row, self.col-i], board, self.color):
                    moves.append((self.row, self.col-i))
                    if board[self.row][self.col-i]:
                        # piece exist
                        if board[self.row][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #right
            i = 1
            while True:
                if is_valid_move([self.row, self.col+i], board, self.color):
                    moves.append((self.row, self.col+i))
                    if board[self.row][self.col+i]:
                        # piece exist
                        if board[self.row][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
        #for black
        if self.color == "b":
            #top
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col], board, self.color):
                    moves.append((self.row-i, self.col))
                    if board[self.row-i][self.col]:
                        # piece exist
                        if board[self.row-i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col], board, self.color):
                    moves.append((self.row+i, self.col))
                    if board[self.row+i][self.col]:
                        # piece exist
                        if board[self.row+i][self.col].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #left
            i = 1
            while True:
                if is_valid_move([self.row, self.col-i], board, self.color):
                    moves.append((self.row, self.col-i))
                    if board[self.row][self.col-i]:
                        # piece exist
                        if board[self.row][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #right
            i = 1
            while True:
                if is_valid_move([self.row, self.col+i], board, self.color):
                    moves.append((self.row, self.col+i))
                    if board[self.row][self.col+i]:
                        # piece exist
                        if board[self.row][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
        return moves
     def __str__(self) -> str:
        if self.color == "w":
            return "white_"+ __class__.__name__
        return "black_"+__class__.__name__

class Bishop(Piece):
     def __init__(self,  row, column, color):
        self.row = row
        self.col = column
        super().__init__( self.row, self.col, color, 3)
    
     def possible_moves(self, board):
        global count
        count+=1
        print(f"count: {count}")
        moves = []
        #white
        if self.color == "w":
            #top-left
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col-i], board, self.color):
                    moves.append((self.row-i, self.col-i))
                    if board[self.row-i][self.col-i]:
                        # piece exist
                        if board[self.row-i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #top-right
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col+i], board, self.color):
                    moves.append((self.row-i, self.col+i))
                    if board[self.row-i][self.col+i]:
                        # piece exist
                        if board[self.row-i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-left
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col-i], board, self.color):
                    moves.append((self.row+i, self.col-i))
                    if board[self.row+i][self.col-i]:
                        # piece exist
                        if board[self.row+i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-right
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col+i], board, self.color):
                    moves.append((self.row+i, self.col+i))
                    if board[self.row+i][self.col+i]:
                        # piece exist
                        if board[self.row+i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
        #black
        if self.color == "b":
            #top-left
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col-i], board, self.color):
                    moves.append((self.row-i, self.col-i))
                    if board[self.row-i][self.col-i]:
                        # piece exist
                        if board[self.row-i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #top-right
            i = 1
            while True:
                if is_valid_move([self.row-i, self.col+i], board, self.color):
                    moves.append((self.row-i, self.col+i))
                    if board[self.row-i][self.col+i]:
                        # piece exist
                        if board[self.row-i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-left
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col-i], board, self.color):
                    moves.append((self.row+i, self.col-i))
                    if board[self.row+i][self.col-i]:
                        # piece exist
                        if board[self.row+i][self.col-i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
            #bottom-right
            i = 1
            while True:
                if is_valid_move([self.row+i, self.col+i], board, self.color):
                    moves.append((self.row+i, self.col+i))
                    if board[self.row+i][self.col+i]:
                        # piece exist
                        if board[self.row+i][self.col+i].color != self.color:
                            # diff color piece exist
                            break
                    i+=1
                    continue
                break
        return moves

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
            if is_valid_move([self.row-2, self.col-1], board, self.color):
                moves.append((self.row-2, self.col-1))
            if is_valid_move([self.row-2, self.col+1], board, self.color):
                moves.append((self.row-2, self.col+1)) 
            #bottom 
            if is_valid_move([self.row+2, self.col-1], board, self.color):
                moves.append((self.row+2, self.col-1))
            if is_valid_move([self.row+2, self.col+1], board, self.color):
                moves.append((self.row+2, self.col+1)) 
            #left
            if is_valid_move([self.row+1, self.col-2], board, self.color):
                moves.append((self.row+1, self.col-2))
            if is_valid_move([self.row-1, self.col-2], board, self.color):
                moves.append((self.row-1, self.col-2)) 
            #right
            if is_valid_move([self.row+1, self.col+2], board, self.color):
                moves.append((self.row+1, self.col+2))
            if is_valid_move([self.row-1, self.col+2], board, self.color):
                moves.append((self.row-1, self.col+2)) 
        if self.color == "b":
            #top
            if is_valid_move([self.row+2, self.col-1], board, self.color):
                moves.append((self.row+2, self.col-1))
            if is_valid_move([self.row+2, self.col+1], board, self.color):
                moves.append((self.row+2, self.col+1)) 
            #bottom 
            if is_valid_move([self.row-2, self.col-1], board, self.color):
                moves.append((self.row-2, self.col-1))
            if is_valid_move([self.row-2, self.col+1], board, self.color):
                moves.append((self.row-2, self.col+1)) 
            #left
            if is_valid_move([self.row+1, self.col-2], board, self.color):
                moves.append((self.row+1, self.col-2))
            if is_valid_move([self.row-1, self.col-2], board, self.color):
                moves.append((self.row-1, self.col-2)) 
            #right
            if is_valid_move([self.row+1, self.col+2], board, self.color):
                moves.append((self.row+1, self.col+2))
            if is_valid_move([self.row-1, self.col+2], board, self.color):
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

     

     def possible_moves(self, board):
        moves = [] # all possible moves (row, col) format
        if self.color == "w":
            
            if self.first_move:
                if is_valid_move_pawn([self.row-1, self.col], board, self.color):
                    moves.append((self.row-1, self.col))
                    if is_valid_move_pawn([self.row-2, self.col], board, self.color):
                        moves.append((self.row-2, self.col))
            else:
                if not board[self.row-1][self.col]:
                    moves.append((self.row-1, self.col))

            #kill move
            # left side
            if (0<=self.row-1<=7) and (0<=self.col-1<=7):
                if board[self.row-1][self.col-1]:
                    #if its not the same color 
                    if board[self.row-1][self.col-1].color != self.color:
                        moves.append((self.row-1, self.col-1))
                    
            # right side
            if (0<=self.row-1<=7) and (0<=self.col+1<=7):
                if board[self.row-1][self.col+1]:
                    #if its not the same color 
                    if board[self.row-1][self.col+1].color != self.color:
                        moves.append((self.row-1, self.col+1))
                    

     
        if self.color == "b":
            if self.first_move:
                if is_valid_move_pawn([self.row+1, self.col], board, self.color):
                    moves.append((self.row+1, self.col))
                    if is_valid_move_pawn([self.row+2, self.col], board, self.color):
                        moves.append((self.row+2, self.col))
            else:
                if not board[self.row+1][self.col]:
                    moves.append((self.row+1, self.col))
            
            #kill move
            # left side
            if (0<=self.row+1<=7) and (0<=self.col-1<=7):
                if board[self.row+1][self.col-1]:
                    #if its not the same color 
                    if board[self.row+1][self.col-1].color != self.color:
                        moves.append((self.row+1, self.col-1))
                    
            # right side
            if (0<=self.row+1<=7) and (0<=self.col+1<=7):
                if board[self.row+1][self.col+1]:
                    #if its not the same color 
                    if board[self.row+1][self.col+1].color != self.color:
                        moves.append((self.row+1, self.col+1))

        return moves
     
    