r1, c1, r2, c2 = map(int, input().split())

maxx = max(abs(r1), abs(c1), abs(r2), abs(c2))
dr = abs(r1 - r2) + 1
dc = abs(c1 - c2) + 1
data = [[1] * dc for _ in range(dr)]
ddr = abs((r1 + maxx) - 0)
ddc = abs((c1 + maxx) - 0)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
sx = maxx + 1
sy = maxx + 1
count = 1
if maxx > 0:
    for i in range(1, 1 + maxx):
        for j in range(4):
            #스타팅 포인트는 (0, 1)
            for k in range(1, 2 * i + 1):
                sx = sx + dx[j]
                sy = sy + dy[j]
                #print(sx, sy)
                count += 1
                if r1 <= sx - maxx <= r2 and c1 <= sy - maxx <= c2:
                    #print(sx, sy)
                    data[sx-ddr][sy-ddc] = count
        sy += 1
        sx += 1

else:
    print(0)
    exit()

max_len = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        max_len = max(max_len, len(str(data[i][j])))
for i in range(len(data)):
    for j in range(len(data[i])):
        print(f'{data[i][j]:>{max_len}d}', end = ' ')
    print()

