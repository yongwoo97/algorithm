#이문제는 밖으로 나간 모래의 양을 구하는것이다.
#단순 구현문제이다

import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [list(map(int,input().split())) for _ in range(n)]

dx = [[1, 2, -1, -2, 1, 1, -1, -1, 0],
       [1, 2, -1, -2, 1, 1, -1, -1, 0],
       [0,0,0,0, 1, 1, -1,-1, 2],
       [0, 0, 0, 0,1, 1,-1,-1,-2]]

dy = [[0, 0 ,0, 0, -1, 1, 1, -1, -2],
       [0, 0 ,0, 0, -1, 1, 1, -1, 2],
       [1,2,-1,-2, 1, -1, 1, -1, 0 ],
       [1, 2, -1,-2, 1, -1, 1, -1, 0]]

per = [[7, 2, 7, 2, 10, 1, 1, 10, 5],
        [7, 2, 7, 2, 1, 10, 10, 1, 5],
        [7,2,7,2, 10, 10, 1, 1,5],
        [7,2,7,2, 1, 1, 10, 10,5]]

dex = [0, 0, 1, -1]
dey = [-1, 1, 0, 0]

import math
out = 0
def tornado(d, x, y):
    global data, out
    total = data[x][y]
    dx1 = dx[d]
    dy1 = dy[d]
    per1 = per[d]
    for i in range(9):
        nx = x + dx1[i]
        ny = y + dy1[i]
        np = per1[i]
        residue = math.floor(data[x][y] * np / 100)

        if 0 <= nx < n and 0 <= ny < n:
            data[nx][ny] += residue
        else:
           # print(residue, 'residue')
            out += residue
        total -= residue

    nx = x + dex[d]
    ny = y + dey[d]
    if 0 <= nx < n and 0 <= ny < n:
        data[nx][ny] += total
    else:
        out += total
    data[x][y] = 0
dd = [0,2,1,3]
counter = 0
forward = 1
sx = n // 2
sy = n // 2

ddx = [0, 1, 0, -1]
ddy = [-1, 0, 1, 0]

for i in range(2*n - 1):
    counter += 1
    di = dd[i%4]
    for j in range(forward):
        nx = sx + ddx[i%4]
        ny = sy + ddy[i%4]

        if ny == -1:
            print(out)
            exit()
        tornado(di, nx, ny)
        sx = nx
        sy = ny
    if counter == 2:
        forward += 1
        counter = 0
#print(out)
