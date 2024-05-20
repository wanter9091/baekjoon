board = [list(map(int, input().split())) for _ in range(9)]

box = []

count = [0]

for r in range(9):
    for c in range(9):
        if not board[r][c]:
            box.append([r, c])


def check(a, b):  # 1,2
    num = board[a][b]
    for i in range(9):
        if i != b and board[a][i] == num:
            return False
        if i != a and board[i][b] == num:
            return False

    s_a, s_b = (a // 3) * 3, (b // 3) * 3

    for i in range(s_a, s_a + 3):
        for j in range(s_b, s_b + 3):
            if i == a and j == b:
                continue
            if board[i][j] == num:
                return False

    return True


def dfs(depth):
    if count[0]:
        return
    if depth == len(box):
        count[0] += 1
        for i in range(9):
            print(*board[i])
        return

    a, b = box[depth]
    for i in range(1, 10):
        board[a][b] = i
        if check(a, b):
            dfs(depth + 1)
        board[a][b] = 0


dfs(0)
