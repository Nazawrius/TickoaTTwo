import time

class Solution:
    def __init__(self):
        self.map = self.create_map(9)
    
    def solve_board(self, board, player):
        code = board.get_code()

        res = self.map[code]
        if res != None:
            return res

        if board.check_win():
            self.map[code] = (-1)**(player + 1)
            return (-1)**(player + 1)

        moves = board.available_moves(player)
        if moves == []:
            self.map[code] = 0
            return 0
        else:
            boards = []
            for move in moves:
                new_board = board.make_copy()
                new_board.make_move(move[0] + 1, move[1] + 1, player)
                boards.append(new_board)
            
            results = [self.solve_board(board, player^1) for board in boards]

            if (-1)**player in results:
                self.map[code] = 1
                return (-1)**player
            if 0 in results:
                self.map[code] = 0
                return 0
            self.map[code] = (-1)**(player + 1)
            return (-1)**(player + 1)
    
    @staticmethod
    def create_map(n):
        def sequence(n):
            if n == 1:
                return ['0', '1', '2', '3']
            
            seq = sequence(n - 1)
            a = ['0' + s for s in seq]
            b = ['1' + s for s in seq]
            c = ['2' + s for s in seq]
            d = ['3' + s for s in seq]
            return [*a, *b, *c, *d]
    
        def check(s):
            p1 = 0
            p2 = 0
            for i in s:
                p1 += int(i) % 2
                p2 += int(i) >= 2

            return p1 == p2 or p1 == p2 + 1        

        return dict((s, None) for s in filter(check, sequence(n)))