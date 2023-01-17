import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

def bfs(a, b):
    global data, n, m, visited

    q = deque()

    q.append([a, b])

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    count = 1


    while q:
        x, y = q.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and data[nx][ny] == 1:
                    q.append([nx, ny])
                    count += 1
                    visited[nx][ny] = 1

    return count

visited = [[0] * m for _ in range(n)]
maxx = 0
num = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 and visited[i][j] == 0:
            num += 1
            visited[i][j] = 1
            maxx = max(maxx, bfs(i, j))
print(num)
print(maxx)