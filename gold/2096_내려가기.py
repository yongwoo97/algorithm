'''
import sys
sys.setrecursionlimit(1000000)
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0,0] for _ in range(n)] for _ in range(3)]

for i in range(n):
    for j in range(3):
        if i == 0:
            dp[j][i][0] = data[i][j]
            dp[j][i][1] = data[i][j]
        else:
            if j == 0:
                dp[j][i][0] = min(dp[j][i-1][0], dp[j+1][i-1][0]) + data[i][j]
                dp[j][i][1] = max(dp[j][i-1][1], dp[j+1][i-1][1]) + data[i][j]
            elif j == 1:
                dp[j][i][0] = min(dp[j-1][i - 1][0], dp[j + 1][i - 1][0], dp[j][i-1][0]) + data[i][j]
                dp[j][i][1] = max(dp[j-1][i - 1][1], dp[j + 1][i - 1][1], dp[j][i-1][1]) + data[i][j]
            else:
                dp[j][i][0] = min(dp[j-1][i - 1][0], dp[j][i - 1][0]) + data[i][j]
                dp[j][i][1] = max(dp[j-1][i - 1][1], dp[j][i - 1][1]) + data[i][j]

maxx = 0
minn = float('inf')

for i in range(3):
    maxx = max(maxx, dp[i][-1][1])
    minn = min(minn, dp[i][-1][0])
#print(dp)
print(maxx, minn)

#틀렸음, dp문제가 아니라 dfs 문제일까나?
#구현해보고 채점은 받아 봐야겠다.
maxx = -1
minn = float('inf')
def dfs(x, y, result):
    global n, data, maxx, minn

    if x == n:
        maxx = max(maxx, result)
        minn = min(minn, result)
        return result
    nresult = result + data[x][y]
    if y == 0:
        dfs(x+1, y, nresult)
        dfs(x+1, y+1, nresult)
    elif y == 1:
        dfs(x + 1, y, nresult)
        dfs(x + 1, y + 1, nresult)
        dfs(x + 1, y - 1, nresult)
    else:
        dfs(x + 1, y - 1, nresult)
        dfs(x + 1, y, nresult)

for i in range(3):
    dfs(0, i, 0)
print(maxx, minn)
'''

import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_dp), min(min_dp))