N = int(input())
W = list(map(int, input().split()))

max_val = [0]


def dfs(l, p):
    if len(l) == 2:
        max_val[0] = max(max_val[0], p)
        return

    for i in range(1, len(l) - 1):
        dfs(l[0:i] + l[i + 1:len(l)], p + (l[i - 1] * l[i + 1]))


dfs(W, 0)

print(max_val[0])
