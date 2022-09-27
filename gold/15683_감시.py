import sys
from itertools import product



input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())

data1 = [list(map(int, input().split())) for _ in range(n)]
cur = []

for i in range(n):
    for j in range(m):
        if data1[i][j] < 6 and data1[i][j] > 0:
            cur.append([i, j])
def cal(a):
    global n, m
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                count += 1
    return count
k = len(cur)
per = list(product([0, 1, 2, 3], repeat=k))

minn = float('inf')

from copy import deepcopy
for e in range(len(per)):
    data = deepcopy(data1)
    for t in range(k):
        a, b = cur[t]

        if data[a][b] == 1:
            if per[e][t] == 0:
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
            elif per[e][t] == 1:
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
            elif per[e][t] == 2:
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
            elif per[e][t] == 3:
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
        if data[a][b] == 2:
            if per[e][t] == 0 or per[e][t] == 1:
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
            elif per[e][t] == 2 or per[e][t] == 3:
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break

        if data[a][b] == 3:
            if per[e][t] == 0:
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
            elif per[e][t] == 1:
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
            elif per[e][t] == 2:
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
            elif per[e][t] == 3:
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
        if data[a][b] == 4:
            if per[e][t] == 0:
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
            elif per[e][t] == 1:
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
            elif per[e][t] == 2:
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(b, -1, -1):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
            elif per[e][t] == 3:
                for i in range(b, m):
                    if data[a][i] == 0:
                        data[a][i] = -1
                    elif data[a][i] == 6:
                        break
                for i in range(a, n):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
                for i in range(a, -1, -1):
                    if data[i][b] == 0:
                        data[i][b] = -1
                    elif data[i][b] == 6:
                        break
        if data[a][b] == 5:
            for i in range(b, m):
                if data[a][i] == 0:
                    data[a][i] = -1
                elif data[a][i] == 6:
                    break
            for i in range(a, n):
                if data[i][b] == 0:
                    data[i][b] = -1
                elif data[i][b] == 6:
                    break
            for i in range(a, -1, -1):
                if data[i][b] == 0:
                    data[i][b] = -1
                elif data[i][b] == 6:
                    break
            for i in range(b, -1, -1):
                if data[a][i] == 0:
                    data[a][i] = -1
                elif data[a][i] == 6:
                    break
    minn = min(minn, cal(data))

print(minn)
