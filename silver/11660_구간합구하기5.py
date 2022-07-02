import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

su = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(k):
        su[i][j] = sum(data[i][:j+1]) + sum)
