import sys

arr_data = [[1, 0, 3, 0, 0, 0, 5, 0, 9],
            [0, 0, 2, 1, 0, 9, 4, 0, 0],
            [0, 0, 0, 7, 0, 4, 0, 0, 0],
            [3, 0, 0, 5, 0, 2, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 0, 5, 0],
            [7, 0, 0, 8, 0, 3, 0, 0, 4],
            [0, 0, 0, 4, 0, 1, 0, 0, 0],
            [0, 0, 9, 2, 0, 5, 8, 0, 0],
            [8, 0, 4, 0, 0, 0, 1, 0, 7]]


#  解法一
def check(i, j, k, arr):
    for n in range(0, 9):
        if arr[i][n] == k or arr[n][j] == k or \
                arr[(i // 3) * 3 + n // 3][(j // 3) * 3 + n % 3] == k:
            return False
    return True


def shudu_dfs(i, j, arr):
    if i == 9:
        for item in arr:
            print(''.join(map(str, item)))
        sys.exit()
    if arr[i][j] > 0:
        shudu_dfs(i if j < 8 else i + 1, (j + 1) % 9, arr)
    if arr[i][j] == 0:
        for k in range(1, 10):
            if check(i, j, k, arr):
                arr[i][j] = k
                shudu_dfs(i if j < 8 else i + 1, (j + 1) % 9, arr)
                arr[i][j] = 0
        return False
    return True


# 定位3*3方块
def square(x, y):
    # m = 3 * (x // 3)
    # n = 3 * (y // 3)
    # for i in range(3):
    #     for j in range(3):
    #         print(i + m, j + n)

    for n in range(9):
        print(x // 3 * 3 + n // 3, y // 3 * 3 + n % 3)


#   解法二
def is_value(board, x, y):
    # 检查填入的坐标是否与行中已有元素相等
    # 列与行是否符合
    for i in range(9):
        if (i != x and board[i][y] == board[x][y]) or \
                (i != y and board[x][i] == board[x][y]):
            return False
    # 检查每个正方形是否符合
    # 以下代码教会了我们如何遍历3*3方块
    m = 3 * (x // 3)
    n = 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                return False
    return True


def solve_shudu_dfs(board):
    # 遍历每一个坐标
    for i in range(9):
        for j in range(9):
            # 找board里的需要填入的位置
            if board[i][j] == 0:
                # 从可选之间选一个
                for k in range(1, 10):
                    board[i][j] = k
                    # 在if的时候调用递归
                    # 如果这个递归可以返回true并且当前填入的数字也没毛病
                    # 则证明我们解完了数独
                    if is_value(board, i, j) and solve_shudu_dfs(board):
                        return True
                    # 到这个位置说明填入的数不太行，所以把它先空着。
                    board[i][j] = 0
                # 进行完当前可选的所有数字都不行，说明上一次决策有问题，返回false
                return False
    # 所有0都填满，并且没毛病，返回true
    return True


def func():
    # 获取输入
    input_data = []
    for i in range(9):
        input_data.append([])
    for item in input_data:
        ss = input()
        for j in ss:
            item.append(int(j))
    # shudu_dfs(0, 0, input_data)
    solve_shudu_dfs(input_data)
    for item in input_data:
        print(''.join(map(str, item)))


# t1 = time.time()
# for item in arr_data:
#     print(''.join(map(str, item)))
# print("===============================")
# solve_shudu_dfs(arr_data)
# for item in arr_data:
#     print(''.join(map(str, item)))
# t2 = time.time()
# print(t2 - t1)
# print("===============================")
# shudu_dfs(0, 0, arr_data)

# 输入值
# 103000509
# 002109400
# 000704000
# 300502006
# 060000050
# 700803004
# 000401000
# 009205800
# 804000107
# 输出值
# 143628579
# 572139468
# 986754231
# 391542786
# 468917352
# 725863914
# 237481695
# 619275843
# 854396127

if __name__ == '__main__':
    pass
    func()

# if __name__ == '__main__':
#     print('1111')
#     pass
# if __name__ == '__main__':
#     print('fsd')
