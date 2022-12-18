import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
from copy import deepcopy

start = 0
def bfs(visiter, x, y):
    global n, m, dx, dy

    q = deque()
    q.append([x, y])
    visiter[x][y] = 1

    while q:

        xx, yy = q.popleft()

        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visiter[nx][ny] == 0 and data[nx][ny] != 0:
                    q.append([nx, ny])
                    visiter[nx][ny] = 1

    return visiter


def checker():
    global n, m, data
    count = 0
    visiter = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and visiter[i][j] == 0:
                count += 1
                bfs(visiter, i, j)

    return count

while True:
    start += 1
    visited = [[0] * m for _ in range(n)]
    c_data = deepcopy(data)
    #아래 코드는 1년이 지날때 마다 빙산을 녹이는 코드
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and data[i][j] != 0:
                count = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if data[ni][nj] == 0:
                        count += 1
                c_data[i][j] -= count
                if c_data[i][j] < 0:
                    c_data[i][j] = 0
    data = c_data

    num_bingsan = checker()

    if num_bingsan >= 2:
        print(start)
        break
    elif num_bingsan == 0:
        print(0)
        break



