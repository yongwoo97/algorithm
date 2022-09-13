import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cur_x, cur_y, cur_d = r, c, d

counter = 0
while True:
    #현재 위치가 청소가 안되어있다면 청소를 해야지
    if data[cur_x][cur_y] == 0:
        data[cur_x][cur_y] = 2
        counter += 1
    #탐색시작
    count = 0

    for i in range(4):
        nd = cur_d - 1
        if nd < 0:
            nd = 3
        nx = cur_x + dx[nd]
        ny = cur_y + dy[nd]
        if data[nx][ny] == 0:
            cur_d = nd
            cur_x = nx
            cur_y = ny
            break
        elif data[nx][ny] == 1 or data[nx][ny] == 2:
            cur_d = nd
            count += 1

    if count == 4:
        nd = (cur_d + 2) % 4
        nx = cur_x + dx[nd]
        ny = cur_y + dy[nd]
        if data[nx][ny] == 1:
            print(counter)
            exit()
        else:
            cur_x = nx
            cur_y = ny
            continue
print(counter)