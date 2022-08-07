import sys
input = sys.stdin.readline
N = [0] * 101
N[1], N[2], N[3] = 1, 1, 1
N[4], N[5] = 2, 2

for i in range(6, 101):
    N[i] = N[i-1] + N[i-5]

t = int(input())
for _ in range(t):
    k = int(input())
    print(N[k])