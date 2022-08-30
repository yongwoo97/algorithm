import sys
from collections import deque

input = sys.stdin.readline
q = deque()

N = int(input())
K = int(input())
m = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    m[x-1][y-1] = 1

L = int(input())
direction = []
for _ in range(L):
    sec, di = input().split()
    direction.append([int(sec), di])

q.append([0, 0])
m[0][0] = -1
i = 0
sec = 0

cur_dix = [0, 1, 0, -1]
cur_diy = [1, 0, -1, 0]
cur_di = 0
tail_q = deque()
tail_q.append([0,0])
while q:
    cur_x, cur_y = q.popleft()
    #print(cur_x, cur_y, 'helo')
    if i < L and sec == direction[i][0]:
        if direction[i][1] == 'D':
            cur_di += 1
            cur_di = cur_di % 4
            i += 1
        elif direction[i][1] == 'L':
            cur_di -= 1
            cur_di = cur_di % 4
            i += 1
    if sec == 0:
        q.append([0, 1])
        tail_q.append([0, 1])
        sec += 1
        continue
    if cur_x < 0 or cur_x > N-1 or cur_y < 0 or cur_y > N - 1:
        print(sec)
        break

    if m[cur_x][cur_y] == 0 and tail_q:
        #print(tail_q)
        tail_x, tail_y = tail_q.popleft()
        m[tail_x][tail_y] = 0


    if m[cur_x][cur_y] == -1:
        print(sec)
        break

    m[cur_x][cur_y] = -1

    next_x = cur_dix[cur_di]
    next_y = cur_diy[cur_di]

    q.append([cur_x+next_x, cur_y+next_y])
    tail_q.append([cur_x+next_x, cur_y+next_y])

    sec += 1

