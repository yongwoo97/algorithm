n, k = map(int, input().split())
import sys
input = sys.stdin.readline

def func(a):
    if a == 1 or a == 0:
        return 1

    return a * func(a-1)

print(int(func(n) / (func(k) * func(n-k))))

