import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().split())
if a < b:
    a, b = b, a
    c, d = d, c

if a == 0 or c == 0:
    print(min(b, d))
elif b == 0 or d == 0:
    print(min(a, c))
else:
    semi = b + 1
    if a < semi:
        print(b * 2)
    elif a == semi:
        print(b + a)
    else:
        print(min(semi * c, a) + b)



