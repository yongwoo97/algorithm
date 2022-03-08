import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    k = int(input())
    data = list(map(int, input().split()))
    d = [0] * k
    for i, j in enumerate(data):
        if i == 0:
            continue
        else:
            d[i] = (d[i-1] * 2) + j

    print(d[-1])
