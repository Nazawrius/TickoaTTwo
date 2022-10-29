from Board import Board

board = Board()
player = 0
print(str(board))
if player:
    print('Player 2:')
else:
    print('Player 1:')

while (s := input()):
    if s == '/restart':
        board = Board()
        player = 0
    
    if len(s) == 3:
        p = s.split(' ')
        if len(p) == 2:
            x, y = p
            if x.isnumeric() and y.isnumeric():
                x, y = int(x), int(y)
                if 1 <= x <= 3 and 1 <= y <= 3:
                    if board.make_move(x, y, player):
                        if board.check_win():
                            print(str(board))
                            if player:
                                print('Player 2 won!')
                            else:
                                print('Player 1 won!')
                            board = Board()
                            player = 0
                        else:
                            player ^= 1
                    else:
                        print('INVALID MOVE!')
    print(str(board))
    print(board.available_moves(player))
    if player:
        print('Player 2:')
    else:
        print('Player 1:')