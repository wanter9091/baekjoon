N = int(input())
S = list(map(int, input().split()))

max_val = 100000 * 20

check = [0] * (max_val + 1)


def dfs(depth, sum_s):
    if depth == N:
        if not check[sum_s]:
            check[sum_s] = True
        return

    dfs(depth + 1, sum_s + S[depth])
    dfs(depth + 1, sum_s)


dfs(0, 0)

for i in range(1, max_val + 1):
    if not check[i]:
        print(i)
        break
