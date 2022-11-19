#일단 모든셀 돌면서 방문했는지 안했는지 확인하기
#만약에 방문하지 않았다면 큐에 넣고 주변 셀 확인해서 가장 높은 셀인지 확인
#같은 셀이라면 같이 큐에 넣고 확인 전부 끝났을 때 가장 높으면 카운트 +1


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

from collections import deque
dx = [0, 1, -1, 0, 1, -1, -1, 1]
dy = [1, 0 , 0, -1, 1, -1, 1, -1]

count = 0

def check(x, y):
    global dx, dy
    visited = [[0] * m for _ in range(n)]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    same = [[x, y]]
    while q:
        nx, ny = q.popleft()

        for i in range(8):
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if 0 <= nnx < n and 0 <= nny < m:
                if data[nx][ny] < data[nnx][nny]:
                    return False, []
                elif data[nx][ny] == data[nnx][nny] and visited[nnx][nny] == 0:
                    q.append((nnx, nny))
                    visited[nx][ny] = 1
                    same.append((nnx, nny))
    return True, same

v = [[0] * m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if v[i][j]:
            continue
        result = check(i, j)
        if result[0]:
            for k, e in result[1]:
                v[k][e] = 1
            count += 1
            #print(i, j)
print(count)


