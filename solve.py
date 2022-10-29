from Solution import Solution
from Board import Board

solution = Solution()

solution.solve_board(Board(), 0)

with open('solution.txt', 'w') as f:
    for code, value in solution.map.items():
        repr = ['_', '|', '-', '+']
        board = '\n'.join(''.join(repr[int(i)] for i in code[3*j:3*j+3]) for j in range(3))
        f.write(f'{board}\n Value: {value}\n')

print(solution.map['000000000'])