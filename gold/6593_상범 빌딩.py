n, m, p = map(int, input().split())

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dz = [1, -1]
def bfs(x, y, z, count, ex, ey, ez):
    global n, m, p
    visited = [[[0] * p for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append([x, y, z, count])
    visited[z][x][y] = 1

    while q:
        x1, y1, z1, c = q.popleft()
        if x1 == ex and y1 == ey and z1 == ez:
            return c

        for e in range(4):
            nx = x1 + dx[e]
            ny = y1 + dy[e]
            if 0 <= nx < m and 0 <= ny < p:
                if visited[z1][nx][ny] == 0 and data[z1][nx][ny] != -1:
                    q.append([nx, ny, z1, c + 1])
                    visited[z1][nx][ny] = 1
        for e in range(2):
            nz = z1 + dz[e]
            if 0 <= nz < n:
                if visited[nz][x1][y1] == 0 and data[nz][x1][y1] != -1:
                    q.append([x1, y1, nz, c + 1])
                    visited[nz][x1][y1] = 1

    return -4



while n != 0 and m != 0 and p != 0:
    data = []
    sx = 0
    sy = 0
    sz = 0
    ex = 0
    ey = 0
    ez = 0
    for e in range(n):
        semi = []
        for j in range(m):
            line = input().rstrip()
            new_line = []
            #print(line)
            for i in range(p):
                if line[i] == 'S':
                    sz = e
                    sx = j
                    sy = i
                    new_line.append(0)
                elif line[i] == '.':
                    new_line.append(0)
                elif line[i] == 'E':
                    new_line.append(-2)
                    ez = e
                    ex = j
                    ey = i
                else:
                    new_line.append(-1)
            semi.append(new_line)
        data.append(semi)
        input()


    result = bfs(sx, sy, sz, 0, ex, ey, ez)
    if result == -4:
        print('Trapped!')
    else:
        print(f'Escaped in {result} minute(s).')



    n, m, p = map(int, input().split())