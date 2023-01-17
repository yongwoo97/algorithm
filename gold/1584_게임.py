import sys
input = sys.stdin.readline

n = int(input())
data = [[0] * 501 for _ in range(501)]

for _ in range(n):
    a, b, c, d = map(int, input().split())

    if a > c:
        if b > d:
            for i in range(d, b + 1):
                for j in range(c, a + 1):
                    data[i][j] = -2
        else:
            for i in range(b, d + 1):
                for j in range(c, a + 1):
                    data[i][j] = -2
    else:
        if b > d:
            for i in range(d, b + 1):
                for j in range(a, c + 1):
                    data[i][j] = -2
        else:
            for i in range(b, d + 1):
                for j in range(a, c+1):
                    data[i][j] = -2

m = int(input())
for _ in range(m):
    a, b, c, d = map(int, input().split())

    if a > c:
        if b > d:
            for i in range(d, b + 1):
                for j in range(c, a + 1):
                    data[i][j] = -3
        else:
            for i in range(b, d + 1):
                for j in range(c, a + 1):
                    data[i][j] = -3
    else:
        if b > d:
            for i in range(d, b + 1):
                for j in range(a, c + 1):
                    data[i][j] = -3
        else:
            for i in range(b, d + 1):
                for j in range(a, c + 1):
                    data[i][j] = -3
from collections import deque
visited = [[0] * 501 for _ in range(501)]
visited[0][0] = 1
dp = [[0] * 501 for _ in range(501)]
def bfs():
    global data, n, m, visited
    q = deque()
    q.append([0, 0])


    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    #그게 최소값을 보장하진 않는다?
    #최적화를 어떻게 할 수 있을까
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 501 and 0 <= ny < 501:
                if visited[nx][ny] == 0 and data[nx][ny] != -3:
                    if data[nx][ny] == 0:
                        visited[nx][ny] = 1
                        dp[nx][ny] = dp[x][y]
                        q.append([nx, ny])
                    elif data[nx][ny] == -2:
                        visited[nx][ny] = 1
                        dp[nx][ny] = dp[x][y] + 1
                        q.append([nx, ny])

                elif visited[nx][ny] == 1 and data[nx][ny] != -3:
                    if data[nx][ny] == 0 and dp[nx][ny] > dp[x][y]:
                        dp[nx][ny] = dp[x][y]
                        q.append([nx, ny])
                    elif data[nx][ny] == -2 and dp[nx][ny] > dp[x][y] + 1:
                        dp[nx][ny] = dp[x][y] + 1
                        q.append([nx, ny])

bfs()
if visited[500][500] == 0:
    print(-1)
else:
    print(dp[500][500])