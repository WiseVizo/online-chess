from Pieces import King, Queen, Rook, Bishop, Knight, Pawn
import pygame

overlap = 0.8
board_x = 147
board_y = 7
sqr = 88
class Board:
    def __init__(self):
        self.board = [[[] for _ in range(8)] for _ in range(8)]

    def fill_board(self):
        # placing both color pawns
        for x in range(8):
            self.board[1][x] = Pawn(1, x, "b")
            self.board[6][x] = Pawn(6, x, "w")

        # placing other peices
        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")

        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")

        #placing king&&queen:
        for x in range(1):
            self.board[0][3] = Queen(0, 3, "b")
            self.board[0][4] = King(0, 4, "b")
            self.board[7][3] = Queen(7, 3, "w")
            self.board[7][4] = King(7, 4, "w")
            
    def draw_board(self, screen, moves):
        for row in range(8):
            for col in range(8):
                # pygame.draw.rect(screen, (255, 0 , 0), (board_x + (col*sqr+col*overlap), board_y + (row*sqr + row*overlap), sqr, sqr), 1)
                if self.board[row][col]:
                    self.board[row][col].draw(screen, self.board, moves)

    def selected_piece(self):
        """
        return: selected_piece obj 
        """
        for row in range(8):
            for col in range(8):
                if self.board[row][col] and self.board[row][col].is_selected():
                    return (self.board[row][col]) 

    
if __name__ == "__main__":
    game_board = Board()
    print(game_board.board)
    print(game_board.fill_board())
    print(game_board.board)

