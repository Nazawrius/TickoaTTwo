class Board:
    def __init__(self):
        self.tiles = [[Tile(i, j) for j in range(3)] for i in range(3)]
    
    def make_move(self, x, y, player):
        tile = self.tiles[x - 1][y - 1]
        if player == 0 and tile.ver:
            tile.set_ver()
            return True
        if player == 1 and tile.hor:
            tile.set_hor()
            return True
        return False
    
    def available_moves(self, player):
        ver, hor = 0, 0
        ver_moves, hor_moves = [], []
        for i in range(3):
            for j in range(3):
                if self.tiles[i][j].hor:
                    hor += 1
                    hor_moves.append((i, j))
                if self.tiles[i][j].ver:
                    ver += 1
                    ver_moves.append((i, j))
        
        if player:
            return hor_moves
        else:
            return ver_moves
    
    def check_win(self):
        win = False
        for row in self.tiles:
            if row[1].state == row[2].state == row[0].state == 3:
                win = True
        
        for i in range(3):
            if self.tiles[1][i].state == self.tiles[2][i].state == self.tiles[0][i].state == 3:
                win = True
        
        if self.tiles[0][0].state == self.tiles[1][1].state == self.tiles[2][2].state == 3:
            win = True

        if self.tiles[2][0].state == self.tiles[1][1].state == self.tiles[0][2].state == 3:
            win = True

        return win
    
    def __str__(self):
        return '\n'.join(''.join(str(tile) for tile in row) for row in self.tiles)
    
    def get_code(self):
        return ''.join(''.join(str(tile.state) for tile in row) for row in self.tiles)
    
    def make_copy(self):
        board = Board()
        board.tiles = [[tile.make_copy() for tile in row] for row in self.tiles]
        return board


class Tile:
    def __init__(self, i, j):
        self.repr = ['_', '|', '-', '+']
        self.state = 0 
        self.x = i
        self.y = j
        self.ver = True
        self.hor = True
    
    def set_hor(self):
        if self.state:
            self.state = 3
        else:
            self.state = 2
        self.hor = False

    def set_ver(self):
        if self.state:
            self.state = 3
        else:
            self.state = 1
        self.ver = False
    
    def __str__(self):
        return self.repr[self.state]
    
    def make_copy(self):
        tile = Tile(self.x, self.y)
        tile.state = self.state
        tile.hor = self.hor
        tile.ver = self.ver
        return tile
        