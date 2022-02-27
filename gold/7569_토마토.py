from collections import deque
a, b, c = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(b)] for _ in range(c)]

q = deque()
move = [(0, 1, 0), (1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

for h in range(c):
    for i in range(b):
        for j in range(a):
            if graph[h][i][j] == 1:
                q.append((j, i, h))

dd = [[[0] * a for _ in range(b)] for _ in range(c)]
day = 0
def bfs():
    global day, move
    while q:
        x, y, z = q.popleft()
        day = max(day, dd[z][y][x])
        for i in move:
            x1, y1, z1 = i
            nx, ny, nz = x + x1, y + y1, z + z1
            if nx >= 0 and nx < a and ny >= 0 and ny < b and nz >= 0 and nz < c:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    dd[nz][ny][nx] = dd[z][y][x] + 1
                    q.append((nx, ny, nz))


if len(q) == 0:
    print(-1)
else:
    bfs()
    for h in range(c):
        for i in range(b):
            for j in range(a):
                if graph[h][i][j] == 0:
                    print(-1)
                    exit()

    print(day)
