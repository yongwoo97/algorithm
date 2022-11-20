import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = []

for _ in range(n):
    line = list(input().rstrip())
    data.append(line)

visited = [[0] * m for _ in range(n)]
ans = 0
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
def dfs(x, y, c):
    global visited, ans, k, data

    if x == 0 and y == m-1 and c == k:
        ans += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != 'T':
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, c + 1)
                visited[nx][ny] = 0
visited[n-1][0] = 1
dfs(n-1, 0, 1)
print(ans)


