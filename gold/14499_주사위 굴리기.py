import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().rstrip().split())
ma = []
sx = x
sy = y
for i in range(n):
    line = list(map(int, input().rstrip().split()))
    ma.append(line)
data = list(map(int, input().rstrip().split()))


def rotate(dice, d):
    if d == 1:
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[1]
    elif d == 2:
        dice[0], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[0], dice[3]
    elif d == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[2]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[5], dice[0], dice[4]
    return dice

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
start = [0, 0, 0, 0, 0, 0]
#print(ma)
for i in range(k):
    di = data[i]
    nx, ny = sx + dx[di], sy + dy[di]
    if 0 <= nx and nx < n and 0 <= ny and ny < m:
        start = rotate(start, di)
        print(start[0])
        if ma[nx][ny] == 0:
            ma[nx][ny] = start[5]
        else:
            start[5] = ma[nx][ny]
            ma[nx][ny] = 0
        sx = nx
        sy = ny
