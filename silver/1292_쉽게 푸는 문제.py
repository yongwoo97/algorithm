import sys
input = sys.stdin.readline
dp = [0] * 1001

i = 1
idx = 1
while idx < 1001:

    for j in range(i):
        dp[idx] = i
        idx += 1
        if idx > 1000:
            break
    i += 1

k = [0] * 1001
for i in range(1, 1001):
    k[i] = dp[i] + k[i-1]

#print(k)
a, b = map(int, input().split())
print(k[b]-k[a-1])
