def check(a, b):  # 세로 가로 입력하면 현재 판에서 문제없는지 알려줌 문제없다면 트루 반환
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


def dfs(d):
    global can, puzzle
    if can:
        return

    if d == zero:
        can += 1
        puzzle += 1
        print("Puzzle", puzzle)
        for i in range(9):
            for j in range(9):
                print(board[i][j], end="")
            print()
        return

    row, col = 0, 0  # 빈칸의 보드 탐색 후 start로 저장
    good = 0
    for i in range(9):
        if good:
            break
        for j in range(9):
            if board[i][j] == 0:
                row, col = i, j
                good = 1
                break

    #가로 타일 넣기
    if good and (col + 1) < 9 and board[row][col + 1] == 0:
        for i in range(1, 10):
            for j in range(1, 10):
                if tile[i][j] == 0:
                    tile[i][j] = 1
                    tile[j][i] = 1
                    board[row][col] = i
                    board[row][col + 1] = j
                    if check(row, col) and check(row, col + 1):
                        dfs(d + 2)
                    board[row][col] = 0
                    board[row][col + 1] = 0
                    tile[i][j] = 0
                    tile[j][i] = 0

    # 세로 타일 넣기
    if good and (row + 1) < 9 and board[row + 1][col] == 0:
        for i in range(1, 10):
            for j in range(1, 10):
                if tile[i][j] == 0:
                    tile[i][j] = 1
                    tile[j][i] = 1
                    board[row][col] = i
                    board[row + 1][col] = j
                    if check(row, col) and check(row + 1, col):
                        dfs(d + 2)
                    board[row][col] = 0
                    board[row + 1][col] = 0
                    tile[i][j] = 0
                    tile[j][i] = 0


puzzle = 0
while True:
    N = int(input())
    if N == 0:
        break

    #스도쿠 보드
    board = [[0] * 9 for _ in range(9)]

    #타일 사용여부 체크:  안쓰는 곳은 2, 사용 안한곳 0, 사용 한곳 1
    tile = [[2] * 10 for _ in range(10)]
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                tile[i][j] = 0

    #입력값 N을 통해 보드와 타일 세팅
    for i in range(N):
        a, b, c, d = input().split()
        tile[int(a)][int(c)] = 1
        tile[int(c)][int(a)] = 1

        board[ord(b[0]) - 65][int(b[1]) - 1] = int(a)
        board[ord(d[0]) - 65][int(d[1]) - 1] = int(c)

    one = [0] + list(input().split())
    for i in range(1, 10):
        one_a = one[i]
        board[ord(one_a[0]) - 65][int(one_a[1]) - 1] = i

    #타일 넣을 수 있는 칸의 수
    zero = 81 - ((2 * N) + 9)

    can = 0
    dfs(0)
