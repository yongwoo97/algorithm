import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

maxx = 0
def dfs(x, y, dis, score, visited):
    global maxx
    if dis == 4:
        maxx = max(maxx, score + data[x][y])

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if dis + 1 <= 4 and visited[nx][ny] == 0:
                dfs(nx, ny, dis + 1, score + data[x][y], visited)
    visited[x][y] = 0

#요철 모양의 도형은 예외처리 해줘야 하나?
v = [[0] * m for _ in range(n)]
sc = 0
for i in range(n):
    for j in range(m):
        dfs(i, j, 1, 0, v)
        if j + 1 < m and j - 1 >= 0:
            if i + 1 < n:
                maxx = max(maxx, data[i][j] + data[i][j+1] + data[i][j-1] + data[i+1][j])
            if i - 1 >= 0:
                maxx = max(maxx, data[i][j] + data[i][j + 1] + data[i][j - 1] + data[i - 1][j])
        if i + 1 < n and i - 1 >= 0:
            if j + 1 < m:
                maxx = max(maxx, data[i][j] + data[i+1][j] + data[i-1][j] + data[i][j + 1])
            if j - 1 >= 0:
                maxx = max(maxx, data[i][j] + data[i+1][j] + data[i-1][j] + data[i][j - 1])
print(maxx)

