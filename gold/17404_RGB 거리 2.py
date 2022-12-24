import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
#dfs로는 자꾸 시간초과가 나네 결국엔 dp로 가야하네
result = float('inf')
'''
if n == 3:
    def dfs(start, x, y, score):
        global data, n, result

        if score >= result:
            return

        if x == n - 2:
            for i in range(3):
                if i != start and i != y:
                    result = min(score + data[x + 1][i], result)
            return
        for i in range(3):
            if i != y:
                dfs(start, x + 1, i, score + data[x + 1][i])


    for i in range(3):
        dfs(i, 0, i, data[0][i])
    print(result)
else:
'''
for k in range(3):
    switch = [0] * 3
    switch[k] = 1

    dp = [[float('inf')] * 3 for _ in range(n)]
    dp[0][k] = data[0][k]


    for i in range(1, n):
        if i == n-1:
      #      print(switch)
            for e in range(3):
                if switch[e] == 1:
                    continue

                else:
                 #   print(e, 'hwer')
                    if e == 0:
                        result = min(dp[i-1][e+1] + data[i][e], dp[i-1][e+2] + data[i][e], result)
                    elif e == 1:
                        result = min(dp[i-1][e-1] + data[i][e], dp[i-1][e+1] + data[i][e], result)
                    else:
                        result = min(dp[i - 1][e - 1] + data[i][e], dp[i - 1][e -2] + data[i][e], result)
                   # print(result, '1hfhsjfhj23')
        else:
            for j in range(3):
               # print(i, j)
                if j == 0:

                    dp[i][j] = min(dp[i-1][j+1] + data[i][j], dp[i-1][j+2] + data[i][j], dp[i][j])
                elif j == 1:
                    dp[i][j] = min(dp[i-1][j-1] + data[i][j], dp[i-1][j+1] + data[i][j], dp[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + data[i][j], dp[i - 1][j -2 ] + data[i][j], dp[i][j])
    switch[k] = 0


  #  for i in dp:
  #      print(*i)
  #  print()

print(result)
