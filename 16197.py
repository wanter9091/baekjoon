N, M = map(int, input().split())  #세로 가로

board = [input() for _ in range(N)]  #가로 M 세로 N

res = [11]


def check(coin):  #떨어졌다면 1반환 아니라면 0반환
    if coin[0] < 0 or coin[0] >= M or coin[1] < 0 or coin[1] >= N:
        return True
    else:
        return False


def can(before, after):  #
    if after[0] < 0 or after[0] >= M or after[1] < 0 or after[1] >= N:
        return after  #떨어졌다면 그 떨어진 위치 그대로 보낸다 (인덱스 범위 벗어나는 오류 방지)
    if board[after[1]][after[0]] == '#':
        return before  #벽이라면 그 이전 위치를 보낸다
    else:
        return after  #이동 가능하다면 이동 한 위치를 보낸다


def dfs(depth, one, two):  #[가로,세로]
    if depth == 11:
        return  #떨구기 실패
    if (check(one) and not check(two)) or (not check(one) and check(two)):
        res[0] = min(depth, res[0])
        return  #depth 값으로 정답 판단
    if check(one) or check(two):
        return  #둘다 떨어진 경우라 그냥 리턴으로 종료

    #상
    dfs(depth + 1, can(one, [one[0], one[1] - 1]), can(two, [two[0], two[1] - 1]))
    #하
    dfs(depth + 1, can(one, [one[0], one[1] + 1]), can(two, [two[0], two[1] + 1]))
    #좌
    dfs(depth + 1, can(one, [one[0] - 1, one[1]]), can(two, [two[0] - 1, two[1]]))
    #우
    dfs(depth + 1, can(one, [one[0] + 1, one[1]]), can(two, [two[0] + 1, two[1]]))


coin = []
for i in range(M):
    for j in range(N):
        if len(coin) < 2 and board[j][i] == 'o':
            coin.append([i, j])

dfs(0,coin[0],coin[1])

if res[0]==11:
    print(-1)
else:
    print(res[0])