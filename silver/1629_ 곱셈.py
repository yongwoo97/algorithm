a, b, c = map(int, input().split())

def func(a1, b1):

    if b1 == 1:
        return a1 % c

    temp = func(a1, b1//2)

    if b1 % 2 == 0:
        return temp * temp % c

    else:
        return temp * temp * a1 % c

print(func(a, b))