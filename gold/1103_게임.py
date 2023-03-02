#완전 탐색 문제인가?
#문제는 사이클이 생길 때 어떤식으로 감지해서 -1을 출력하느냐이다

n, m = map(int, input().split())
data = []
for _ in range(n):
    line = list(input().rstrip())
    data.append(line)

visited = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maxx = 1
def dfs(x, y, count):
    global data, visited, maxx
    if x < 0 or y < 0 or x >= n or y >= m:
        return
    if data[x][y] == 'H':
        return

    for i in range(4):
        nx = x + (dx[i] * int(data[x][y]))
        ny = y + (dy[i] * int(data[x][y]))
        if 0 <= nx < n and 0 <= ny < m:

            if visited[nx][ny] == 1:
                print(-1)
                exit()
            else:
                if data[nx][ny] != 'H':
                    visited[nx][ny] = 1
                    maxx = max(maxx, count + 1)
                    dfs(nx, ny, count + 1)
                    visited[nx][ny] = 0
dfs(0, 0, 1)
print(maxx)