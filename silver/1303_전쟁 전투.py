m, n = map(int, input().split())
data = []
for _ in range(n):
    line = list(input().rstrip())
    data.append(line)
visited = [[0] * m for _ in range(n)]

from collections import deque
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def bfs(x, y):

    global visited, n, m, data, dx, dy
    q = deque()
    cur = data[x][y]
    visited[x][y] = 1
    q.append((x, y))
    count = 0

    while q:
        i, j = q.popleft()
        count += 1
        for e in range(4):
            ni = i + dx[e]
            nj = j + dy[e]
            if 0 <= ni < n and 0 <= nj < m:
                if visited[ni][nj] == 0 and data[ni][nj] == cur:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
    return count
r = [0, 0]
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            result = bfs(i, j)
            if data[i][j] == 'W':
                r[0] += result ** 2
            else:
                r[1] += result ** 2
print(*r)