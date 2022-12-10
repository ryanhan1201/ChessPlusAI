class Pawn(self):
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __init__(self, player = int, x = int, y = int):
        self.PLAYER = player
        self.POS = (x, y)
        self.INITPOS = (x, y)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(player = int, r = int, c = int, grid = [[]]):
        retList = []
        #TODO: Check for the which player first
        if player == 1:
            if r < len(grid) - 1 and grid[r + 1][c] == Empty:
                retList.append((r + 1, c))
            if r < len(grid) - 1 and c < len(grid) and grid[r + 1][c + 1] != Empty:
                retList.append((r + 1, c + 1))
            if r < len(grid) - 1 and c > 0 and grid[r + 1][c - 1] != Empty:
                retList.append((r + 1, c - 1))
        else:
            if r > 0 and grid[r - 1][c] == Empty:
                retList.append((r - 1, c))
            if r > 0 and c > 0 and grid[r - 1][c - 1] != Empty:
                retList.append((r + 1, c + 1))
            if r > 0 and c < len(grid) - 1 and grid[r - 1][c + 1] != Empty:
                retList.append((r + 1, c - 1))
        return retList
class Rook(self):
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(player = int, r = int, c = int, grid = [[]]):
        retList = []
        for row in range(0, len(grid)):
            if grid[row][c] != Empty:
                retList.append((row, c))
        for col in range(0, len(grid)):
            if grid[r][col] != Empty:
                retList.append((r, col))
        return retList
        
class Knight(self):
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(x, y):
        
class Bishop(self):
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(x, y):
        
class Queen(self):
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(x, y):
        
class King(self):
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __init__(self, player, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(x, y):
        
class Empty(self):
    POS = (0, 0)
    def __init(self, r = int, c = int):
        self.POS = (r, c)
