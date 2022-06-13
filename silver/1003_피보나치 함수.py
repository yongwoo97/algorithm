import sys
input = sys.stdin.readline
n = int(input().rstrip())

data = [int(input()) for _ in range(n)]

zero_count = [1, 0]
one_count = [0, 1]

def fibo(n):
    global zero_count, one_count

    if n < len(zero_count):
        return zero_count[n], one_count[n]

    for i in range(len(zero_count), n + 1):
        zero_count.append(zero_count[i-2] + zero_count[i-1])
        one_count.append(one_count[i-2] + one_count[i-1])

    return zero_count[n], one_count[n]





for i in data:

    a, b = fibo(i)
    print(a, b)
