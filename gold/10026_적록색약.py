
from collections import deque


n = int(input())
data = [list(input().rstrip()) for _ in range(n)]

dx = [0,1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
def bfs1(x, y, cur_color):


    q.append([x, y])

    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and data[nx][ny] == cur_color:
                    q.append([nx, ny])
                    visited[nx][ny] = 1


count = 0
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs1(i, j, data[i][j])
            count += 1
print(count, end=' ')
count = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if data[i][j] == 'R':
            data[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs1(i, j, data[i][j])
            count += 1
print(count)
