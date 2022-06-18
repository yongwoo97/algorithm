import math

start = int(input())

data = [list(map(int, input().split())) for _ in range(start)]

#print(data)


def func(x, y, n):
    global data
    semi = [0, 0, 0]

    if n == 1:
        semi[data[x][y] + 1] += 1
        #print(semi)
        return semi

    temp = data[x][y]
    check = False

    for i in range(n):
        for j in range(n):
            if temp != data[x + i][y + j]:
                check = True
                break

    if check:
        nn = n // 3
        for i in range(0, n, nn):
            for j in range(0, n, nn):
                #print(x+i, y+j)
                semi_result = func(x + i, y + j, nn)

                semi[0] += semi_result[0]
                semi[1] += semi_result[1]
                semi[2] += semi_result[2]

        return semi

    semi[temp + 1] += 1
    return semi

result = func(0,0,start)
for i in result:
    print(i)
#print(func(0,0,start))