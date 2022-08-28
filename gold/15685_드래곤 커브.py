import sys
input = sys.stdin.readline

n = int(input())
m = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x,y,d,g = map(int,input().split())
    m[y][x] = 1
    memo = []
    for i in range(g+1):

        if i == 0:
            if d == 0:
                m[y][x+1] = 1
                x += 1
            elif d == 1:
                m[y-1][x] = 1
                y -= 1
            elif d == 2:
                m[y][x-1] = 1
                x -= 1
            else:
                m[y+1][x] = 1
                y += 1
            memo.append(d)
            continue
        memo1 = memo[::-1]
        #print(memo1)
        for j in memo1:
            dd = 0
            if j == 0:
                m[y-1][x] = 1
                y -= 1
                dd = 1
            elif j == 1:
                m[y][x-1] = 1
                x -= 1
                dd = 2
            elif j == 2:
                m[y+1][x] = 1
                y += 1
                dd = 3
            else:
                m[y][x+1] = 1
                x += 1
                dd = 0
            memo.append(dd)

count = 0
for i in range(100):
    for j in range(100):
        if m[i][j] == 1:
            if m[i+1][j] == 1 and m[i][j+1] == 1 and m[i+1][j+1] == 1:
                count += 1
print(count)