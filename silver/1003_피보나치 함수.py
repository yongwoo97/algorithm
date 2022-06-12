import sys
input = sys.stdin.readline
n = int(input().rstrip())

data = [int(input()) for _ in range(n)]



def fibo(n):
    global zero_count, one_count
    if n != 0 and n != 1:
        return fibo(n - 1) + fibo(n - 2)
    if n == 0:
        zero_count += 1
        return 0
    elif n == 1:
        one_count += 1
        return 1


for i in data:
    zero_count = 0
    one_count = 0
    fibo(i)

    print(zero_count, one_count)
