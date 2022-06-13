n = int(input())

def check(k):

    x1, y1, r1, x2, y2, r2 = k[0], k[1], k[2], k[3], k[4], k[5]

    r_sum = r1 + r2
    r_dis = abs(r1 - r2)

    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d == 0 and r_dis == 0:
        return -1
    if d < r_dis:
        return 0
    elif d == r_dis:
        return 1
    elif d > r_dis and d < r_sum:
        return 2
    elif d == r_sum:
        return 1
    else:
        return 0


for i in range(n):
    data = list(map(int, input().split(' ')))
    print(check(data))
