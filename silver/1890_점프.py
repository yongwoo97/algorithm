#그냥 규칙에 맞게 dfs
#1st trial에서 시간초과
#결국엔 memo이용해라 이 이야기임
#

import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0]
dy = [0, 1]
from collections import deque

count = 0
visited = [[0] * n for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def dfs(x, y):
    global count, dx, dy, data, visited
    if x == n-1 and y == n-1:
        return 1

    if dp[x][y] != 0:
        return dp[x][y]

    for i in range(2):
        nx = x + (dx[i] * data[x][y])
        ny = y + (dy[i] * data[x][y])
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dp[x][y] += dfs(nx, ny)
                visited[nx][ny] = 0
    if dp[x][y] == 0:
        return 0
    else:
        return dp[x][y]
dfs(0, 0)
print(dp[0][0])

