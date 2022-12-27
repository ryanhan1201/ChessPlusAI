class Pawn:
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __str__(self):
        return "P"
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
            if r < len(grid) - 1 and c < len(grid) and not grid[r + 1][c + 1] == Empty:
                retList.append((r + 1, c + 1))
            if r < len(grid) - 1 and c > 0 and not grid[r + 1][c - 1] == Empty:
                retList.append((r + 1, c - 1))
        else:
            if r > 0 and grid[r - 1][c] == Empty:
                retList.append((r - 1, c))
            if r > 0 and c > 0 and not grid[r - 1][c - 1] == Empty:
                retList.append((r + 1, c + 1))
            if r > 0 and c < len(grid) - 1 and not grid[r - 1][c + 1] == Empty:
                retList.append((r + 1, c - 1))
        return retList

#TODO: CONSIDER THE CASES WHEN YOU TAKE THE PEICE
#Think about the castling possibility
class Rook:
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    CASTLE = False #Tells if this rook is castleable
    MOVED = False
    def __str__(self):
        return "R"
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
        if (r == 0 and c == 7) or (r == 7 and c == 7):
            self.CASTLE = True
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(r = int, c = int, grid = [[]]):
        retList = []
        up = True
        down = True
        left = True
        right = True
        for i in range(0, len(grid)):  
            if not up and not down and not left and not right:
                break
            if r < len(grid) - i and grid[r + i][c] == Empty:
                retList.append((r + i, c))
            else:
                up = False
                if r < len(grid) - i:
                    retList.append((r + i, c))
            if r - i >= 0 and grid[r - i][c] == Empty:
                retList.append((r + i, c))
            else:
                down = False
                if r - i >= 0:
                    retList.append((r - i, c))
            if c < len(grid) - i and grid[r][c + i] == Empty:
                retList.append((r, c + i))
            else:
                right = False
                if c < len(grid) - i:
                    retList.append((r, c + i))
            if c - i >= 0 and grid[r][c - i] == Empty:
                retList.append((r, c - i))
            else:
                left = False
                if c - i >= 0:
                    retList.append((r, c - i))
        return retList
        #check to see if castling is allowed
    def notMove(self):
        return self.INITPOS == self.POS
    def castle(self, king):
        if self.CASLTE and self.notMove and king.notMove():
            return True
            #Make it so that castling is possible


class Knight:
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __str__(self):
        return "Kn"
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(r = int, c = int, grid = [[]]):
        retList = []
        if r < len(grid) - 2:
            if c < len(grid) - 1:
                retList.append((r + 2, c + 1))
            if c - 1 >= 0 and grid[r + 2][c - 1]:
                retList.append((r + 2, c - 1))
        if r - 2 >= 0:
            if c < len(grid) - 1 and grid[r - 2][c + 1]:
                retList.append((r - 2, c + 1))
            if c - 1 >= 0 and grid[r - 2][c - 1]:
                retList.append((r - 2, c - 1))
        if c < len(grid) - 2:
            if r < len(grid) - 1 and grid[r + 1][c + 2]:
                retList.append((r + 1, c + 2))
            if r - 1 >= 0 and grid[r - 1][c + 2]:
                retList.append((r - 1, c + 2))
        if c - 2 >= 0:
            if r < len(grid) - 1 and grid[r + 1][c - 2]:
                retList.append((r + 1, c - 2))
            if r - 1 >= 0 and grid[r - 1][c - 2]:
                retList.append((r - 1, c - 2))
        return retList

class Bishop:
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __str__(self):
        return "B"
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(r = int, c = int, grid = [[]]):
        retList = []
        upRight = True
        upLeft = True
        downRight = True
        downLeft = True
        #proabbaly just use 4 for loops to generate the legal spaces
        for i in range(len(grid)):
            if not upRight and not upLeft and not downRight and not downLeft:
                break
            if r < len(grid) - i:
                if c < len(grid) - i and upRight:
                    retList.append((r + i, c + i))
                else:
                    retList.append((r + i, c + i))
                    upRight = False
                if c - i >= 0 and upLeft:
                    retList.append((r + i, c + i))
                else:
                    retList.append((r + i, c + i))
                    upLeft = False
            if r - i >= 0:
                if c < len(grid) - i and downRight:
                    retList.append((r-+ i, c + i))
                else:
                    retList.append((r - i, c + i))
                    downRight = False
                if c - i >= 0 and downLeft:
                    retList.append((r - i, c + i))
                else:
                    retList.append((r - i, c + i))
                    downLeft = False
        return retList

class Queen:
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __str__(self):
        return "Q"
    def __init__(self, player = int, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    def legalMoves(r = int, c = int, grid = [[]]):
        retList = Rook.legalMoves(r, c, grid)
        for coor in Bishop.legalMoves(r, c, grid):
            retList.append(coor)
        return retList
        
class King:
    PLAYER = ""
    POS = (0, 0)
    INITPOS = (0, 0)
    def __str__(self):
        return "K"
    def __init__(self, player, r = int, c = int):
        self.PLAYER = player
        self.POS = (r, c)
        self.INITPOS = (r, c)
    
    """
    Returns true if the king hasnt moved
    """
    def notMove(self):
        return self.INITPOS == self.POS
    """
    Input: current x, y position, and current state of the board
    Return: A list of all the valid moves
    """
    #Need to think about being in check and stuff
    #will do later
    #thnk  about castling too
    #have a checker for castling is possible, like check if the king has moved
    # def legalMoves(x, y):
        
class Empty:
    POS = (0, 0)
    def __init__(self, r = int, c = int):
        self.POS = (r, c)
    def __str__(self):
        return " "
