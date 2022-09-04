import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())

mapp = [[0] * m for _ in range(n)]
for _ in range(k):
    x, y, x1, y1 = map(int, input().split())
    for i in range(y, y1):
        for j in range(x, x1):
            mapp[i][j] = 1

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    space = 0
    mapp[x][y] = 1
    while q:
        x, y = q.popleft()
        space += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if mapp[nx][ny] == 0:
                    q.append([nx,ny])
                    mapp[nx][ny] = 1
    return space

semi = []
count = 0
for i in range(n):
    for j in range(m):
        if mapp[i][j] == 0:
            s = bfs(i, j)
            count += 1
            semi.append(s)

print(count)
semi.sort()
print(*semi)