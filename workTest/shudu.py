def is_value(board, x, y):
    for i in range(9):
        if (i != x and board[i][y] == board[x][y]) or (i != y and board[x][i] == board[x][y]):
            return False
    m = 3 * (x // 3)
    n = 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                return False
    return True


def solve_shudu_dfs(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1, 10):
                    board[i][j] = k
                    if is_value(board, i, j) and solve_shudu_dfs(board):
                        return True
                    board[i][j] = 0
                return False
    return True


# 1 0 3 0 0 0 5 0 9
# 0 0 2 1 0 9 4 0 0
# 0 0 0 7 0 4 0 0 0
# 3 0 0 5 0 2 0 0 6
# 0 6 0 0 0 0 0 5 0
# 7 0 0 8 0 3 0 0 4
# 0 0 0 4 0 1 0 0 0
# 0 0 9 2 0 5 8 0 0
# 8 0 4 0 0 0 1 0 7

while True:
    try:
        input_data = []
        for i in range(9):
            input_data.append([])
        for i in range(9):
            in_list = input().split(' ')
            for j in in_list:
                input_data[i].append(int(j))
        solve_shudu_dfs(input_data)
        for item in input_data:
            print(' '.join(map(str, item)))
    except:
        break
