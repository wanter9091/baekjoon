N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))
ope = ['+', '-', '*', '/']
max_res = [-(1e+9)]
min_res = [1e+9]


def cal(s):
    val = A[0]
    for i in range(N - 1):
        if s[i] == ope[0]:
            val += A[i + 1]
        elif s[i] == ope[1]:
            val -= A[i + 1]
        elif s[i] == ope[2]:
            val *= A[i + 1]
        elif s[i] == ope[3]:
            if val < 0:
                val = -((-val) // A[i + 1])
            else:
                val //= A[i + 1]
    return val


def dfs(depth, s):
    if depth == N-1:
        val = cal(s)
        if max_res[0] < val:
            max_res[0] = val
        if min_res[0] > val:
            min_res[0] = val
        return

    for i in range(4):
        if O[i]:
            O[i] -= 1
            dfs(depth + 1, s + [ope[i]])
            O[i] += 1


dfs(0, [])
print(max_res[0])
print(min_res[0])
