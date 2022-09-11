import sys
input = sys.stdin.readline



def combination(a, b):

    if b == 0:
        return "아무것도 안뽑았습니다."
    if b == len(a):
        return [a]
    if b == 1:
        result = []
        for i in a:
            result.append([i])
        return result

    result = []
    for i in range(len(a)):
        pivot = [a[i]]
        semi = combination(a[i+1:], b-1)
        #print(semi)

        for j in semi:
            result.append(pivot+j)
    return result



n, m, d = map(int, input().split())
save = [list(map(int, input().split())) for _ in range(n)]
data = [i for i in range(m)]
a = combination(data, 3)
def clean():
    global mmap
    count = 0
    for i in range(n):
        for j in range(m):
            if mmap[i][j] == 1:
                count += 1

    if count == 0:
        return True
    else:
        mmap = [[0] * m] + mmap[:n-1]
        return False

from collections import deque
dx = [0, -1, 0]
dy = [-1, 0, 1]
def attack(x, y, dis):
    global mmap, m, n
    q = deque()
    target = []
    visited = [[0] * m for _ in range(n)]

    q.append([x, y, dis])
    visited[x][y] = 1
    while q:
        x1, y1, nd = q.popleft()

        if mmap[x1][y1] == 1:
            #만약에 적군이 있으면 배열에 넣어주고 target return 해야지
            target.append([x1, y1])
            return target

        for i in range(3):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < n and 0 <= ny < m and nd + 1 <= d:
                if not visited[nx][ny]:
                    q.append([nx, ny, dis + 1])
                    visited[nx][ny] = 1

mmax = 0

from copy import deepcopy

for k in a:
    mmap = deepcopy(save)
    enemy = 0
    #print(k)
    while True:

        result = []
        for j in k:
            semi = attack(n-1, j, 1)
            if semi:
                result += semi
        if result:
            for i in result:
                x, y = i
                if mmap[x][y] == 1:
                    mmap[x][y] = 0
                    enemy += 1

        c = clean()
        if c:
            break

    mmax = max(mmax, enemy)



print(mmax)