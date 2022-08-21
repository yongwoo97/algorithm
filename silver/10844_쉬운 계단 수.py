n = int(input())
dp = [0] * 10

def func(k):
    global dp
    newdp = [0] * 10
    if k == 1:
        for i in range(1, 10):
            newdp[i] = 1
    else:
        for i in range(10):
            if i == 0:
                newdp[i+1] += dp[i]
                continue
            elif i == 9:
                newdp[i-1] += dp[i]
                continue

            newdp[i+1] += dp[i]
            newdp[i-1] += dp[i]
    dp = newdp
for i in range(1, n+1):
    func(i)
#print(dp)
print(sum(dp) % 1000000000)