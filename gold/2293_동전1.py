#일단 dfs로 풀어볼까?
#시간 초과가 나진 않을것 같은데... 흠
#dpf, dp일수도 있나?

n, m = map(int, input().split())
data = []
for _ in range(n):
    a = int(input())
    data.append(a)

dp = [0] * 10001
dp[0]= 1
for i in data:
    for j in range(i, m+1):
        dp[j] += dp[j-i]

print(dp[m])