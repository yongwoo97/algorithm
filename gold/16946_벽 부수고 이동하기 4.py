import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data = [list(map(int, list(input().rstrip()))) for _ in range(n)]
from copy import deepcopy
from collections import deque

dx = [1, 0 ,-1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]
def bfs( x, y):
    global n, m, dx, dy, data, visited



    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    count = 0
    while q:
        x1, y1 = q.popleft()
        count += 1
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and data[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = 1
    return count

sub = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            c = bfs(i, j)
            sub[i][j] = c
for i in sub:
    print(''.join(list(map(str, i))))