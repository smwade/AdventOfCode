
class Board:
    def __init__(self, board):
        self.board = board
        self.state = [[0]*5]*5
        self.state = [[0 for i in range(5)] for j in range(5)]
        self.row_counts = [0]*5
        self.col_counts = [0]*5
        self.win = False

    def mark(self, x):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == x:
                    self.state[row][col] = 1
                    self.row_counts[row] += 1
                    self.col_counts[col] += 1
                    if self.row_counts[row] == 5 or self.col_counts[col] == 5:
                        self.win = True

    def calc_score(self, last_num):
        score = 0
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.state[row][col] == 0:
                    score += self.board[row][col]
        return score * last_num

    def print_board(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                print(board[row][col], end=' ')
            print("")


def play_game(boards, draws):
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.win == True:
                return board.calc_score(draw)

def loose_game(boards, draws):
    num_boards = len(boards)
    num_boards_win = 0
    for draw in draws:
        for board in boards:
            if board.win == False:
                board.mark(draw)
                if board.win == True:
                    num_boards_win += 1
                    if num_boards_win == num_boards:
                        return board.calc_score(draw)

# prepare data
with open('day_4.txt') as f:
    raw_data = f.readlines()

draws = [int(x) for x in raw_data[0].split(',')]

boards = []
board = []
for r in raw_data[2:]:
    if r == '\n':
        boards.append(Board(board))
        board = []
    else:
        board.append([int(x) for x in r.split()])
boards.append(Board(board))

print(play_game(boards, draws))
print(loose_game(boards, draws))

