import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

s = 0
dp = [0]
for i in data:
    s += i
    dp.append(s)

i = 0
j = 1
ans = 100001

while i != n:
    if dp[j] - dp[i] >= k:
        if j - i < ans:
            ans = j - i
        i += 1
    else:
        if j != n:
            j += 1
        else:
            i += 1

if ans != 100001:
    print(ans)
else:
    print(0)