class Piece:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.position = (self.row, self.column)
        self.color
        self.selected = False
        self.image

    def is_selected(self):
        return self.selected
    
    def move(self):
        pass

    def draw(self):
        pass

class King(Piece):
    pass
class Queen(Piece):
    pass
class Rook(Piece):
    pass
class Bishop(Piece):
    pass
class Knight(Piece):
    pass
class Pawn(Piece):
    pass

        
        
