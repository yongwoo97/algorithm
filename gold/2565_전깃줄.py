import sys
input = sys.stdin.readline

n = int(input())
data = [-1] * 506
for _ in range(n):
    a, b = map(int, input().split())
    data[a] = b

dp = [0] * 506

maxx = 0
for i in range(501):
    cur = data[i]
    for j in range(i-1, -1, -1):
        if data[j] == -1 and j != 0:
            continue
        if data[j] < cur:
            dp[i] = max(dp[i], dp[j] + 1)


    maxx = max(maxx, dp[i])

print(n-maxx)