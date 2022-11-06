n, a, b, c, d = map(int, input().split())

data = [a, b, c, d]
answer = 0
mapp1 = [[0]* 50 for _ in range(50)]
mapp1[25][25] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
count1 = 0
def dfs(count, x, y, per):
    global n, a, b, c, d, answer, count1, mapp1

    if count == n:
        answer += per
        count1 += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if mapp1[nx][ny] == 0 and data[i] != 0:
            mapp1[nx][ny] = 1
            dfs(count + 1, nx, ny, per * (data[i] / 100) )
            mapp1[nx][ny] = 0
dfs(0, 25, 25, 1)

print(answer)