import sys
input = sys.stdin.readline

data = [list(map(int, input().split())) for _ in range(10)]


from collections import deque
dx = [0, 1, 1]
dy = [1, 1, 0]
from copy import deepcopy
def search(x, y):
    global data

    q = deque()
    q.append((x, y))

    for i in range(1, 6):
        temp = deque()
        while q:
            sx, sy = q.popleft()
            for j in range(3):
                nx = sx + dx[j]
                ny = sy + dy[j]
                if 0 <= nx < 10 and 0 <= ny < 10 and data[nx][ny] == 1:
                        temp.append((nx, ny))
                else:
                    return i
        q = deepcopy(temp)
    return 5

def maxer():
    cur = {i:[] for i in range(1, 6)}

    for i in range(10):
        for j in range(10):
            if data[i][j] == 1:
                semi = search(i, j)
                if not cur[semi]:
                    cur[semi].append((i, j))
    for i in range(5, 0, -1):
        if cur[i]:
            return i, cur[i][0]


    return -1, (-1, -1)
count = 0
counter = {i:5 for i in range(1, 6)}
while True:
    width, cor = maxer()
    if width == -1:
        print(count)
        break
    elif counter[width] == 0:
        print(-1)
        break

    counter[width] -= 1
    count += 1

    nx = cor[0]
    ny = cor[1]
    for i in range(width):
        for j in range(width):
            data[nx + i][ny + j] = 0
