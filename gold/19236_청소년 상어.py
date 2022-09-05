import sys
input = sys.stdin.readline

mmap = [[] for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        mmap[i].append([line[2 * j], line[2 * j + 1]-1])

maxx = 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
from copy import deepcopy
def dfs(x, y, score, mm):
    global maxx
    score += mm[x][y][0]
    maxx = max(maxx, score)
    mm[x][y][0] = 0

    for i in range(1, 17):
        xx = -1
        yy = -1
        for e in range(4):
            for k in range(4):
                if mm[e][k][0] == i:
                    xx = e
                    yy = k
                    break

        if xx != -1 and yy != -1:
            di = mm[xx][yy][1]
            for j in range(8):
                ndi = (di + j) % 8
                nx = xx + dx[ndi]
                ny = yy + dy[ndi]
                if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == x and ny == y):
                    mm[xx][yy][1] = ndi
                    mm[nx][ny], mm[xx][yy] = mm[xx][yy], mm[nx][ny]
                    break

    dis = mm[x][y][1]
    for i in range(1, 4):
        nnx = x + (dx[dis] * i)
        nny = y + (dy[dis] * i)
        if 0 <= nnx < 4 and 0 <= nny < 4 and mm[nnx][nny][0] > 0:
            dfs(nnx, nny, score, deepcopy(mm))

dfs(0, 0, 0, mmap)
print(maxx)