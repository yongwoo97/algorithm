#일단 재귀로 한번 풀어보자

def check(data, x, y, num):

    for i in range(9):
        if y == i:
            continue
        elif num == data[x][i]:
            return False
    for i in range(9):
        if x == i:
            continue
        elif num == data[i][y]:
            return False

    nx = x // 3
    ny = y // 3

    for i in range(3 * nx, nx * 3 + 3):
        for j in range(3 * ny, ny * 3 + 3):
            if i == x and j == y:
                continue
            elif num == data[i][j]:
                return False

    return True

def finish(data):
    for i in range(9):
        x_sum = 0
        y_sum = 0
        for j in range(9):
            x_sum += data[j][i]
            y_sum += data[i][j]
        if x_sum != 45 or y_sum != 45:
            return False

    for i in range(3):

        for j in range(3):
            s_sum = 0
            for e in range(3 * i, 3 * i + 3):
                for k in range(3 * j, 3 * j + 3):
                    s_sum += data[e][k]


            if s_sum != 45:
                return False

    return True

def finish1(data):
    for i in range(9):
        for j in range(9):
            if data[i][j] == 0:
                return False
    return True

result = 0

def recur(mapp, x, y):
    global result
   # print(x, y)
    for i in range(9):
        for j in range(9):
            if mapp[i][j] == 0:
                for e in range(1, 10):
                    if check(mapp, i, j, e):
                        mapp[i][j] = e
                   #     for t in mapp:
                   #         print(t)
                   #     print()
                        if finish(mapp):
                            result = mapp
                            for t in result:
                                print(''.join(list(map(str, t))))
                        #    print(result)
                            exit()
                        recur(mapp, i, j)

                    mapp[i][j] = 0
                return
import sys
input = sys.stdin.readline

d = []
for _ in range(9):
    line = list(input().rstrip())
    line = list(map(int,line))
    d.append(line)
#print(d)
recur(d, 0, 0)
#for i in result:
 #   print(i)
#for i in result:
  #  print(i)