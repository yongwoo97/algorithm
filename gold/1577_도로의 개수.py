import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
data = [list(map(int,input().split())) for _ in range(k)]
for i in range(k):
    data[i][0] = abs(data[i][0] - n)
    data[i][2] = abs(data[i][2] - n)

#위 오른쪽
dx = [-1, 0]
dy = [0, 1]
dp = [[0] * (m+1) for _ in range(n+1)]
dp[n][0] = 1
visited = [[0] * (m+1) for _ in range(n+1)]
#print(data)
def function():
    start_x = n
    start_y = 0

    q = deque()
    q.append([start_x, start_y])
    visited[start_x][start_y] = 1
    while q:
        x, y = q.popleft()
      #  print(x,y)
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n + 1 and 0 <= ny < m + 1:
                #if visited[nx][ny] == 0:
                #고장난 도로인지 체크하기
                check = False
                for j in data:
                    if [x, y, nx, ny] == j or [nx, ny, x, y] == j:
                       # print([x, y, nx, ny], j)
                        check = True
                        #print(check)
                        break
               # print(check)
                if check:
                    continue
                else:
                    if visited[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = 1
                    dp[nx][ny] += dp[x][y]

function()
print(dp[0][m])