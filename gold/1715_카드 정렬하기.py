import sys
n = int(input())
data = []
for _ in range(n):
    line = int(input().rstrip())
    data.append(line)

dp = [[0] * n for _ in range(n)]


result = 0
for d in range(n):
    minn = float('inf')
    for i in range(n-d):
        j = i + d
        if i == j:
            dp[i][j] = data[i]
        else:
            dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
        if d > 0:
            minn = min(minn, dp[i][j])
  #  print(minn)
    result += minn

print(result)