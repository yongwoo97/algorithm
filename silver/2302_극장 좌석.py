n = int(input())
m = int(input())
vip = []
seat = [0] * (n + 1)
for _ in range(m):
    vip.append(int(input()))

cur = 1
result = 1
dp = [0] * (50)
dp[0] = 1
dp[1] = 1
dp[2] = 2


for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

for i in vip:
    result *= dp[i-cur]
    cur = i + 1

result *= dp[n - cur + 1]
print(result)
