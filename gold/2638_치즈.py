import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def transform(x, y, data):
    global n, m, dx, dy

    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    return_arr = deepcopy(data)

    while q:
        x1, y1 = q.popleft()
        if data[x1][y1] == 0:
            return_arr[x1][y1] = 3
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    if data[nx][ny] == 3 or data[nx][ny] == 0:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
    return return_arr

def melt(arr):
    global n, m, dx, dy
    new_arr = deepcopy(arr)
    for i in range(n):
        for j in range(m):
            count = 0
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if arr[ni][nj] == 3:
                        count += 1
            if count >= 2:
                new_arr[i][j] = 0
    return new_arr

def check(arr):
    global n, m

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                return False
    return True

counter = 0
while True:
    arr1 = transform(0, 0, data)
    arr1 = melt(arr1)
    data = arr1
    counter += 1
    if check(arr1):
        print(counter)
        break
    else:
        continue


