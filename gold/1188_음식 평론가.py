#좀재밌어 보이는 문제네.
a ,b = map(int, input().split())

if a // b >= 1 and a % b == 0:

    print(0)
elif a < b:

    if  b // a == 1:
        print(1 * a)
    else:
        print((b//a - 1) * a)
else:
    re = a % b

    print(re * (a-1))


