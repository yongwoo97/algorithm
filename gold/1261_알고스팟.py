#이문제의 핵심은 무엇일까
#벽을 부수어야 하는 최소 값을 찾는것인데...
#최단경로에서 벽이 몇개 있는지 세는게 중요한가?
#벽을 하나씩 제거하면서 해나가야 하나?
#1초에 128mb인데 가능할까?  벽은 몇개일 것이며?
#가끔은 단순한 방법이 최고일 수 있지
#완탐으로는 안풀리네
#bfs돌면서 벽부술수 있는 카운트가 있다면? 이게 연산이 많이 줄것같긴하다.

# BFS 벽을 최소 몇 개 부수어야 하는가?
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

m,n = map(int, input().split())
arr = [ list(map(int, input())) for _ in range(n)]
dist = [[-1] * m for _ in range(n)]  # 가중치

q = deque()
q.append((0,0))
dist[0][0] = 0
while q:
    x,y = q.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    q.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
print(dist[n-1][m-1])
