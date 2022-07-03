import sys
input = sys.stdin.readline

data = [[[0] * 101 for _ in range(101)] for _ in range(101)]

def func(a, b, c):
    global data
    a1 = a + 50
    b1 = b + 50
    c1 = c + 50
    if data[a1][b1][c1] != 0:
        return data[a1][b1][c1]


    if a <= 0 or b <= 0 or c <= 0:
        data[a1][b1][c1] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        data[a1][b1][c1] = func(20, 20, 20)
        return data[a1][b1][c1]
    elif a < b and b < c:
        data[a1][b1][c1] = func(a, b, c-1) + func(a, b-1, c-1) - func(a, b-1, c)
        return data[a1][b1][c1]
    else:
        data[a1][b1][c1] = func(a-1, b, c) + func(a-1, b-1, c) + func(a-1, b, c-1) - func(a-1, b-1, c-1)
        return data[a1][b1][c1]

while True:
    a1, b1, c1 = map(int, input().split())
    if a1 == -1 and b1 == -1 and c1 == -1:
        break

    result = func(a1, b1, c1)
    print(f'w({a1}, {b1}, {c1}) = {result}')