import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
test = []

for _ in range(k):
    test.append(list(map(int, input().split())))


su = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            su[i][j] = data[i][j]
        elif i == 0:
            su[i][j] = data[i][j] + su[i][j-1]
        elif j == 0:
            su[i][j] = data[i][j] + su[i-1][j]
        else:
            su[i][j] = data[i][j] - su[i-1][j-1] + su[i-1][j] + su[i][j-1]

for i in test:
    x1, y1, x2, y2 = i
    if x1 == x2 and y1 == y2:
        result = data[x2 - 1][y2 - 1]
    elif x1 == 1 and y1 == 1:
        result = su[x2-1][y2-1]
    elif x1 == 1:
        result = su[x2-1][y2-1] - su[x2-1][y1-2]
    elif y1 == 1:
        result = su[x2-1][y2-1] - su[x1-2][y2-1]
    else:
        result = su[x2-1][y2-1] - (su[x1-2][y2-1] + su[x2-1][y1-2]) + su[x1-2][y1-2]
    print(result)