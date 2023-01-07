#이건 어떤문제일까 의도가 무엇일까?
#일단 어디에 끼워 넣어야 할지 위치는 고려할 필요가 없잖아 안그래? 횟수만 고려하면 되니까
#mid 잡고 i, j로 양옆 돌아가면서 세볼까?

n = int(input())
data = list(map(int, input().split()))
datar = data[::-1]

dp = [[0] * (n+1) for _ in range(n+1)]

maxx = 1

for i in range(n):
    for j in range(n):
        if data[i] == datar[j]:
            dp[i+1][j+1] = max(dp[i][j] + 1, dp[i][j+1], dp[i+1][j])

        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        maxx = max(dp[i + 1][j + 1], maxx)

print(n - maxx)