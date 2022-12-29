#합분해
#dp dfs문제일것 같아

n, k = map(int, input().split())
dp = [[0] * 201 for _ in range(201)]

def dfs(a, b):
    global dp, n, k

    if b == 1:
        dp[b][a] = 1
        return 1

    if dp[b][a] != 0:
        return dp[b][a]

    for i in range(a+1):
        dp[b][a] += (dfs(a-i, b-1))
    dp[b][a] %= 1000000000
    return dp[b][a]
dfs(n, k)

print(dp[k][n])