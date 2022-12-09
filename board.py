import piece
"""
Player 1 = White Pieces
Player 2 = Black Pieces
"""
class World():
    LENGTH = 8
    HEIGHT = 8
    GRID = [[]]
    def __init__(self):
        self.GRID = [[]]
    def setup(self):
        #Bottom is White Side
        #Top should be Black Side
        #Bottom Left should be a,1
        for r in range(self.HEIGHT):
            eachRow = []
            for c in range(self.LENGTH):
                eachRow.append(piece.Empty(r, c))
            self.GRID.append(eachRow)
        #BLACK PIECES
        self.GRID[7][0] = piece.Rook(2, 7, 0)
        self.GRID[7][1] = piece.Knight(2, 7, 1)
        self.GRID[7][2] = piece.Bishop(2, 7, 2)
        self.GRID[7][3] = piece.Queen(2, 7, 3)
        self.GRID[7][4] = piece.King(2, 7, 4)
        self.GRID[7][5] = piece.Bishop(2, 7, 5)
        self.GRID[7][6] = piece.Knight(2, 7, 6)
        self.GRID[7][7] = piece.Rook(2, 7, 7)
        #Doing Panws
        for c in range(self.LENGTH):
            self.GRID[7][c] = piece.Pawn(2, 7, 0)
        #WHITE PIECES
        self.GRID[0][0] = piece.Rook(1, 0, 0)
        self.GRID[0][1] = piece.Knight(1, 0, 1)
        self.GRID[0][2] = piece.Bishop(1, 0, 2)
        self.GRID[0][3] = piece.King(1, 0, 3)
        self.GRID[0][4] = piece.Queen(1, 0, 4)
        self.GRID[0][5] = piece.Bishop(1, 0, 5)
        self.GRID[0][6] = piece.Knight(1, 0, 6)
        self.GRID[0][7] = piece.Rook(1, 0, 7)
        #Doing Panws
        for c in range(self.LENGTH):
            self.GRID[0][c] = piece.Pawn(1, 0, c)

    
