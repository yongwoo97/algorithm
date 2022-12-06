#전형적인 bfs문제다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mapp = []
for _ in range(n):
    line = list(input().rstrip())
    mapp.append(line)


from collections import deque

maxx = 0
def bfs(x, y, cur):
    global n, m, mapp, visited, maxx

    if mapp[x][y] == 'W':
        return

    visited = [[0] * m for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    q.append([x, y, cur])
    visited[x][y] = 1

    while q:
        x1, y1, count = q.popleft()
        #print(x1, y1, count)
        maxx = max(count, maxx)
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0<= nx < n and 0 <= ny < m:
                if mapp[nx][ny] == 'L' and visited[nx][ny] == 0:
                    q.append([nx, ny, count + 1])
                    visited[nx][ny] = 1


for i in range(n):
    for j in range(m):
        bfs(i, j, 0)
print(maxx)
