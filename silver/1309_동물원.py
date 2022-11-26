n = int(input())
data = [[0, 0] for _ in range(n)]

dx = [0 ,1, -1, 0]
dy = [1, 0, 0, -1]
result = 0

def func(x, y, count):
    global data, result, n
    if count == 0:
        result += 1
        return

    if 0 <= x < n and 0 <= y < 2:
        for i in range(x, n):
            for j in range(0, 2):
                if data[i][j] == 0:
                    check = False
                    for e in range(4):
                        nx = i + dx[e]
                        ny = j + dy[e]
                        if 0 <= nx < n and 0 <= ny < 2:
                            if data[nx][ny] == 1:
                                check = True
                    if not check:
                        data[i][j] = 1
                        func(i, j, count - 1)
                        data[i][j] = 0


    return

for k in range(1, n+1):
    for i in range(n):
        for j in range(2):
            data[i][j] = 1
            func(i, j, k-1)
            data[i][j] = 0


print(result+1)