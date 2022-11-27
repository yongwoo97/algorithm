n, s, m = map(int, input().split())
data = list(map(int, input().split()))
dp = [[-1] * (m+1) for _ in range(n+1)]

dp[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if dp[i][j] != -1:
            if j + data[i] <= m:
                dp[i+1][j+data[i]] = 1
            if j - data[i] >= 0:
                dp[i+1][j-data[i]] = 1
answer = -1
for i in range(m+1):
    if dp[-1][i] == 1:
        answer = max(answer, i)
print(answer)