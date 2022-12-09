import piece

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
                eachRow.append(piece.EMPTY)
            self.GRID.append(eachRow)
        #BLACK PIECES
        self.GRID[7][0] = piece.ROOK
        self.GRID[7][1] = piece.KNIGHT
        self.GRID[7][2] = piece.BISHOP
        self.GRID[7][3] = piece.QUEEN
        self.GRID[7][4] = piece.KING
        self.GRID[7][5] = piece.BISHOP
        self.GRID[7][6] = piece.KNIGHT
        self.GRID[7][7] = piece.ROOK

        #WHITE PIECES
        self.GRID[0][0] = piece.ROOK
        self.GRID[0][1] = piece.KNIGHT
        self.GRID[0][2] = piece.BISHOP
        self.GRID[0][3] = piece.QUEEN
        self.GRID[0][4] = piece.KING
        self.GRID[0][5] = piece.BISHOP
        self.GRID[0][6] = piece.KNIGHT
        self.GRID[0][7] = piece.ROOK
