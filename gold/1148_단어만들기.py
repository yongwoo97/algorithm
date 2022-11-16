import sys
input = sys.stdin.readline

data = []
board = []
while True:
    line = input().rstrip()
    if line == '-':
        break
    data.append(line)

from copy import deepcopy

while True:
    line = input().rstrip()
    if line == '#':
        break
    board = dict()
    for i in line:
        if i in board:
            board[i] += 1
        else:
            board[i] = 1

    board1 = deepcopy(board)

    maxx = 0
    minn = float('inf')

    for k in board1:
        important = k
        check = False
        for i in data:
            for j in i:
                if j in board1 and board1[j] > 0:
                    board[j] -= 1
                else:
                    break

    data.append(line)

