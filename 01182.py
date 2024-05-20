n, s = map(int, input().split())
ex = list(map(int, input().split()))

count = [0]

def dfs(depth, s_sum):
    if depth == n:
        if s_sum == s:
            count[0] += 1
        return
    dfs(depth + 1, s_sum + ex[depth])
    dfs(depth + 1, s_sum)


dfs(0, 0)
if count[0]>0 and s==0:
    count[0]-=1
print(count[0])
