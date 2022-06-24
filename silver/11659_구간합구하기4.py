import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int, input().split()))

s = [0] * (len(data) + 1)
for i in range(1,n+1):
    s[i] = s[i-1] + data[i-1]

for i in range(m):
    a, b = map(int, input().split())
    result = s[b] - s[a-1]
    print(result)