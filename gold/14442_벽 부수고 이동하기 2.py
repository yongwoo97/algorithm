import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(n)]
#visited = [[0] * m for _ in range(n)]
road = [[float('inf')] * m for _ in range(n)]
road[0][0] = 1
from collections import deque
q = deque()
q.append((0, 0, 0))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
if n == 1 and m == 1:
    print(1)
    exit()
while q:
    x, y, z = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < n and 0 <= ny < m:
            if road[nx][ny] > road[x][y] + 1 and data[nx][ny] == 0:
                road[nx][ny] = road[x][y]+1
                q.append((nx, ny, z))
            elif road[nx][ny] > road[x][y] + 1 and data[nx][ny] == 1 and z < k:
                q.append((nx, ny, z+1))
                road[nx][ny] = road[x][y] + 1

for i in road:
    print(i)
if road[n-1][m-1] == float('inf'):
    print(-1)
else:
    print(road[n-1][m-1])


          #  if visited[nx][ny] == 0 and data[nx][ny] == 0:
        #        q.append((nx, ny, s+1, k))
        #    elif visited[nx][ny] == 0 and data[nx][ny] == 1 and z < k:
         #      q.append((nx, ny, s+1, k+1))
         #   elif visited[nx][ny] == 1:
          #      if data[nx][ny] == 0 and road[nx][ny]