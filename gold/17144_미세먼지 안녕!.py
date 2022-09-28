import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]

machine = []

for i in range(n):
    for j in range(m):
        if data[i][j] == -1:
            machine.append([i, j])

from collections import deque
def scan(k):
    q = deque()
    for i in range(n):

        for j in range(m):
            if k[i][j] != -1 and k[i][j] != 0:
               q.append([i, j])
    return q

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
from copy import deepcopy
for i in range(t):
    cp = [[0] * m for _ in range(n)]
    cp[machine[0][0]][machine[0][1]] = -1
    cp[machine[1][0]][machine[1][1]] = -1

    q = scan(data)
    for x, y in q:
        count = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != -1:
                cp[nx][ny] += int(data[x][y] / 5)
                count += 1
        data[x][y] -= int(data[x][y] / 5) * count
        cp[x][y] += data[x][y]

    data = deepcopy(cp)
    fr = machine[0][0]
    sr = machine[1][0]
   # print(data)
    for x in range(fr-1, -1, -1):
        if data[x+1][0] != -1:
            data[x+1][0] = data[x][0]
    data[0] = data[0][1:]
    #print(data)
    data[0].append(0)
    #print(data)
    for x in range(1, fr+1):
        data[x-1][m-1] = data[x][m-1]

    data[fr] = [-1, 0] + data[fr][1:-1]

    for x in range(sr+1, n):
        if data[x-1][0] != -1:
            data[x-1][0] = data[x][0]
    data[n-1] = data[n-1][1:]
    data[n-1].append(0)

    for x in range(n-1, sr, -1):
        data[x][-1] = data[x-1][-1]
    data[sr] = [-1, 0] + data[sr][1:-1]
   # for y in data:
    #    print(*y)
    #break
result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] != -1:
            result+= data[i][j]
print(result)