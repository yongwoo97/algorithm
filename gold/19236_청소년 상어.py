'''
import sys
input = sys.stdin.readline

dic = {i: [] for i in range(1, 16)}
mmap = []
for i in range(4):
    line = list(map(int, input().split()))
    mm = []
    for j in range(4):
        a1, b1 = 2 * j, 2 * j + 1
        dic[line[a1]] = [i, j, line[b1]]
        mm.append(line[a1])
    mmap.append(mm)

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1,0, 1, 1, 1]

def mulgo(mm, dic):
    for i in dic:
        if i == -1:
            continue
        #만약 물고기가 먹히지 않았다면
        if dic[i]:
            while True:
                nx = dic[i][0] + dx[dic[i][2]]
                ny = dic[i][1] + dy[dic[i][2]]
                if 0 <= nx < 4 and 0 <= ny < 4 and mm[nx][ny] != -1:
                    break

                dic[i][2] += 1
                if dic[i][2] > 8:
                    dic[i][2] = 1

            #물고기가 존재하면
            if mm[nx][ny]:
                temp = mm[nx][ny]
                mm[nx][ny], mm[dic[i][0]][dic[i][1]] = mm[dic[i][0]][dic[i][1]], mm[nx][ny]
                dic[i][0], dic[i][1], dic[temp][0], dic[temp][1] = dic[temp][0], dic[temp][1], dic[i][0], dic[i][1]
            #물고기가 존재하지 않으면
            else:
                mm[nx][ny], mm[dic[i][0]][dic[i][1]] = mm[dic[i][0]][dic[i][1]], mm[nx][ny]
                dic[i][0] = nx
                dic[i][1] = ny

    return mm, dic

score = 0
start_sc = mmap[0][0]
dic[-1] = [0, 0, dic[mmap[0][0]][2]]
dic[mmap[0][0]] = None
mmap[0][0] = -1
mmap, dic = mulgo(mmap, dic)
print()
for i in mmap:
    print(*i)
print()
print(dic)
from copy import deepcopy
def dfs(x, y, di, s, m, dd):
    global dx, dy, score
    nx, ny = x + dx[di], y + dy[di]
    if nx < 0 or ny < 0 or nx > 3 or ny > 3:
        score = max(score, s)
        return

    check = 0
    for i in range(1, 4):
        nx, ny = x + (dx[di] * i), y + (dy[di] * i)
        if 0 <= nx < 4 and 0 <= ny < 4:
            if not m[nx][ny]:
                check += 1
        else:
            check += 1
    if check == 3:
        score = max(score, s)
        return
    for i in range(1, 4):
        mcopy = deepcopy(m)
        ddcopy = deepcopy(dd)
        nx, ny = x + (dx[di] * i), y + (dy[di] * i)
        if 0 <= nx < 4 and 0 <= ny < 4:
            if mcopy[nx][ny]:
                s += mcopy[nx][ny]
                mcopy[x][y], mcopy[nx][ny] = mcopy[nx][ny], mcopy[x][y]
                ddcopy[mcopy[x][y]], ddcopy[mcopy[nx][ny]] = ddcopy[mcopy[nx][ny]], ddcopy[mcopy[x][y]]
                ddcopy[mcopy[x][y]] = None
                mcopy[x][y] = None



                mcopy, ddcopy = mulgo(mcopy, ddcopy)
                dfs(ddcopy[-1][0], ddcopy[-1][1], ddcopy[-1][2], s, mcopy, ddcopy)

dfs(0, 0, dic[-1][2], start_sc, mmap, dic)
print(dic)
print(score)

'''

# 청소년 상어 - BOJ 19236
# DFS+구현
import copy

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish


max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1:
            continue
        f_d = board[f_x][f_y][1]

        for i in range(8):
            nd = (f_d+i) % 8
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            board[f_x][f_y][1] = nd
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]
    for i in range(1, 4):
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))

dfs(0, 0, 0, board)
print(max_score)