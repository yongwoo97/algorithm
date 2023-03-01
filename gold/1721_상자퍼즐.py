import sys
input = sys.stdin.readline
data = []
n = int(input())
nn = n ** 2

for _ in range(nn):
    line = list(map(int, input().split()))
    data.append(line)

from collections import deque

def calc(d, count):
    q = deque(d)
    for _ in range(count):
        x = q.pop()
        q.appendleft(x)
    return list(q)

answer = [[0] * n for _ in range(n)]

answer_top = [[[0] * 5 for _ in range(n)] for _ in range(n)]
visited = [0] * nn
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

from copy import deepcopy

def func(pos_x, pos_y):
    global data, visited, answer, answer_top, n, nn
    #print(pos_x, pos_y)
    if pos_x >= n or pos_y >= n:
        for h in range(n):
            for w in range(n):
                print(answer_top[h][w][0], end = ' ')
            print()
        for h in range(n):
            for w in range(n):
                print(answer[h][w], end = ' ')
            print()
        exit()
        return
    #일단 여기서 모든 큐브를 다 확인하긴 하겠지.
    #만약 이미 사용한 것이라면 continue

    #print(visited)
    for i in range(nn):

        if visited[i] == 1:
            continue

        #일단 가장자리인지 확인부터 해야겠지
        for j in range(4):
            cube = calc(deepcopy(data[i][1:]), j)
            if pos_x == 0:
                if cube[0] != 0:
                    continue
            if pos_y == 0:
                if cube[3] != 0:
                    continue
            if pos_x == n-1:
                if cube[2] != 0:
                    continue
            if pos_y == n-1:
                if cube[1] != 0:
                    continue

            check = False
            for e in range(4):
                nx = pos_x + dx[e]
                ny = pos_y + dy[e]
                if 0 <= nx < n and 0 <= ny < n:
                    if answer_top[nx][ny][0] != 0:
                        if e == 0:
                            if answer_top[nx][ny][4] != cube[1]:
                                check = True
                                break
                        if e == 1:
                            if answer_top[nx][ny][1] != cube[2]:
                                check = True
                                break
                        if e == 2:
                            if answer_top[nx][ny][3] != cube[0]:
                                check = True
                                break
                        if e == 3:
                            if answer_top[nx][ny][2] != cube[3]:
                                check = True
                                break
            if not check:
                visited[i] = 1
                answer_top[pos_x][pos_y] = [data[i][0]] + cube
                answer[pos_x][pos_y] = j

                if pos_y == n-1:
                    func(pos_x + 1, 0)
                elif pos_y < n-1:
                    func(pos_x, pos_y + 1)
                answer_top[pos_x][pos_y] = [0] * 5
                answer[pos_x][pos_y] = 0
                visited[i] = 0

func(0, 0)
