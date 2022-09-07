dp = [0] * 251
dp[0] = 1
dp[1] = 1
dp[2] = 3
for i in range(3, 251):
    dp[i] = dp[i-1] + 2 * dp[i-2]
try:
    while True:
        line = int(input().rstrip())
        print(dp[line])
except:
    pass