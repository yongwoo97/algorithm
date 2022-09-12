import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dx = [1,0,-1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y):

    visited = [[0] * n for _ in range(m)]
    result = [[0] * n for _ in range(m)]
    q = deque()
    q.append([x,y, 0])
    visited[x][y] = 1
    while q:
        x1, y1, dis = q.popleft()
        result[x1][y1] = dis
        for i in range(4):
            nx = x1 + dx[i]
            ny = y1 + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if data[nx][ny] != -1 and visited[nx][ny] == 0:
                    q.append([nx, ny, dis + 1])
                    visited[nx][ny] = 1

    return result


#가설1 그리디하게 최단거리에 있는것들부터 청소해나간다.
while True:

    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    data = [list(input().rstrip()) for _ in range(m)]


    sx = -1
    sy = -1
    target = []
    for i in range(m):
        for j in range(n):
            if data[i][j] == 'o':
                sx = i
                sy = j
                data[i][j] = 0
            elif data[i][j] == '.':
                data[i][j] = 0
            elif data[i][j] == 'x':
                data[i][j] = -1
            else:
                #2는 먼지의 위치
                target.append([i, j])
                data[i][j] = -2

    num = len(target)
    score = 0
    dist_map = [[float('inf')] * (num + 1) for _ in range(num + 1)]
    target = [[sx, sy]] + target

    for k in range(num + 1):

        sx = target[k][0]
        sy = target[k][1]
        r = bfs(sx, sy)

        for e in range(num + 1):
            if k == e:
                dist_map[k][e] = 0
            else:
                nx = target[e][0]
                ny = target[e][1]

                if r[nx][ny] == 0:
                    continue

                dist_map[k][e] = r[nx][ny]
                dist_map[e][k] = r[nx][ny]

    floyd = [[float('inf')] * (num + 1) for _ in range(num+1)]

    for i in range(num+ 1):
        for j in range(num + 1):
            if i == j:
                floyd[i][j] = 0
                continue
            for e in range(num + 1):
                if floyd[i][j] > dist_map[i][e] + dist_map[e][j]:
                    floyd[i][j] = dist_map[i][e] + dist_map[e][j]

    p = list(permutations([i for i in range(1, num + 1)]))
    ans = float('inf')
    for i in p:
        dist = 0
        for j in range(len(i)):
            if j == 0:
                dist += floyd[0][i[j]]
            else:
                dist += floyd[i[j-1]][i[j]]
        if ans > dist:
            ans = dist
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

    #여기서 예외처리가 좀 잘못된것 같아.
    #어떻게하면 예외처리를 제대로 할 수 있지?
    #그리디하게 접근하는게 아니네




