n, x, y, x1, y1 = map(int, input().split())
r = []
if x1 < x or y1 < y:
    print(-1)
elif x == x1:
    if n >= (y1 - y):
        print('U' * (y1 - y) + 'R' * (n - y1 + y))
    else:
        print('U' * n)
elif y == y1:
    print('R' * n)
else:
    check = False
    r_a = 0
    r_b = 0
    result = '-1'
    for i in range(1, n):
        a = n - i
        b = i

        dif_x = x1 - x
        dif_y = y1 - y

        moc_a = dif_x // a
        moc_b = dif_y // b
       # print(moc_a, moc_b)
        if abs(moc_a - moc_b) == 0:

            r_a = dif_x - (moc_a * a)
            r_b = dif_y - (moc_b * b)
            result = 'R' * r_a + 'U' * r_b + 'R' * (a - r_a) + 'U' * (b - r_b)
            r.append(result)


        elif abs(moc_a - moc_b) == 1:

            if moc_a < moc_b:
                if dif_x % a == 0 and dif_y % b == 0:
                    moc_b -= 1
                elif dif_x % a == 0 and dif_y % b != 0:
                    continue
                elif dif_x % a != 0 and dif_y % b == 0:
                    moc_b -= 1
                else:
                    continue
                r_a = dif_x - (moc_a * a)
                r_b = dif_y - (moc_b * b)
                result = 'R' * r_a + 'U' * r_b + 'R' * (a - r_a) + 'U' * (b - r_b)
            else:
                if dif_x % a == 0 and dif_y % b == 0:
                    moc_a -= 1
                elif dif_x % a == 0 and dif_y % b != 0:
                    moc_a -= 1
                elif dif_x % a != 0 and dif_y % b == 0:
                    continue
                else:
                    continue
                r_a = dif_x - (moc_a * a)
                r_b = dif_y - (moc_b * b)
                result = 'R' * r_a + 'U' * r_b + 'R' * (a - r_a) + 'U' * (b - r_b)
            r.append(result)
    if not r:
        print(-1)
    else:
       # print(r)
        r.sort()

        print(r[0])