import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    for i in range(n):
        tx, ty, tz = data[i]

        dis1 = math.sqrt(abs(tx-x1) ** 2 + abs(ty-y1) ** 2)
        dis2 = math.sqrt(abs(tx-x2) ** 2 + abs(ty-y2) ** 2)

        if dis1 < tz and dis2 < tz:
            continue
        elif dis1 > tz and dis2 < tz:
            count += 1
        elif dis1 < tz and dis2 > tz:
            count += 1

    print(count)