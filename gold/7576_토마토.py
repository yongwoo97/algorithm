from collections import deque
a, b = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(b)]

q = deque()
day = 0
dd = [[0] * a for _ in range(b)]
#일단 익은 토마토가 어디있는지 확인해야겠지

for i in range(b):
    for j in range(a):
        if d[i][j] == 1:
            q.append((j, i))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global day, dx, dy, q, d
    while q:
        x1, y1 = q.popleft()
        d[y1][x1] = 1
        day = max(dd[y1][x1], day)
        for i in range(4):
            if y1 + dy[i] >= b or x1 + dx[i] >= a or y1 + dy[i] < 0 or x1 + dx[i] < 0:
                continue
            elif d[y1 + dy[i]][x1 + dx[i]] == -1 or d[y1 + dy[i]][x1 + dx[i]] == 1:
                continue
            else:
                dd[y1 + dy[i]][x1 + dx[i]] = dd[y1][x1] + 1
                q.append((x1 + dx[i], y1 + dy[i]))

if len(q) == 0:
    print(0)
else:
    bfs()
    for i in d:
        if 0 in i:
            print(-1)
            exit()

print(day)