import sys
from collections import deque

input = sys.stdin.readline
n = int(input())



def bfs(x, y, ex, ey, mapp, size):
    q = deque()
    itterr = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (2, -1), (1, -2)]
    q.append((x, y))

    while q:
        curx, cury = q.popleft()
        if curx == ex and cury == ey:
            print(mapp[cury][curx])
            break
        else:
            for i, j in itterr:
                if 0 <= curx + i < size and 0 <= cury + j < size and mapp[cury + j][curx + i] == 0:
                    mapp[cury+j][curx+i] = mapp[cury][curx] + 1
                    q.append((curx + i, cury + j))



for _ in range(n):
    size = int(input())
    mapp = [[0] * size for _ in range(size)]
    startx, starty = map(int, input().split())
    endx, endy = map(int, input().split())
    bfs(startx, starty, endx, endy, mapp, size)
