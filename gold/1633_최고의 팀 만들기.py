import heapq

q = []
i = 0
while True:
    try:
        line = list(map(int,input().split()))
        if not line:
            break
        else:
            q.append(line)
        i += 1
    except EOFError:
        break
dp = [[[0] * 16 for _ in range(16)] for _ in range(1001)]
dp[0][1][0] = q[0][0]
dp[0][0][1] = q[0][1]
result = 0
for i in range(1, len(q)):

    for x in range(16):
        for y in range(16):
            if x < 15:
                if dp[i][x+1][y] < dp[i-1][x][y] + q[i][0]:
                    dp[i][x+1][y] = dp[i-1][x][y] + q[i][0]
            if y < 15:
                if dp[i][x][y+1] < dp[i-1][x][y] + q[i][1]:
                    dp[i][x][y + 1] = dp[i-1][x][y] + q[i][1]
            if dp[i][x][y] < dp[i-1][x][y]:
                dp[i][x][y] = dp[i-1][x][y]
    result = max(result, dp[i][15][15])
print(result)



