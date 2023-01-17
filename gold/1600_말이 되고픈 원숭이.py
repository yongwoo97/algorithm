
import sys
input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

from collections import deque


def bfs():
    global data, n, m, k

    dp = [[[float('inf')] * 31 for _ in range(m)] for _ in range(n)]
    q = deque()

    q.append([0,0,0,0])

    dx = [1, 0, -1, 0]
    dx1 = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [0, 1, 0, -1]
    dy1 = [1, -1, 1, -1, 2, -2, 2, -2]
    dp[0][0] = [0] * m

    while q:

        c, h, x, y = q.popleft()
        if x == n-1 and y == m-1:
            return dp[x][y][h]


        for j in range(8):
            nx = x + dx1[j]
            ny = y + dy1[j]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and h < k and dp[nx][ny][h+1] == float('inf'):
                    dp[nx][ny][h+1] = c + 1
                    q.append([c + 1, h + 1, nx, ny])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0 and dp[nx][ny][h] == float('inf'):
                    dp[nx][ny][h] = c + 1
                    q.append([c+1, h, nx, ny])

    return -1
r = bfs()
print(r)

