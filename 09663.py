N = int(input())
Q = [-1] * N
count = [0]


def check(row):  #서로 공격하면 False 아니면 True
    for i in range(row):
        if Q[i] != -1:
            if Q[i] == Q[row]:
                return False
            if Q[i] == (Q[row] - abs(row - i)) or Q[i] == (Q[row] + abs(row - i)):
                return False
    return True


"""
[2][3] (0,1)(0,5) (1,2)(1,4) (3,2)(3,4) (4,1)(4,5)

"""


def dfs(depth):
    if depth == N:
        count[0] += 1
        return

    for i in range(N):
        Q[depth] = i
        if check(depth):
            dfs(depth + 1)
        Q[depth] = -1


dfs(0)

print(count[0])

"""

문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


"""
