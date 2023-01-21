#에라토테네스의 체 쓰고
#투포이넡로 접근한다.
n = int(input())
dp = [0, 0]
dp1 = [1] * (n-1)

dp = dp + dp1

p = []
for i in range(2, n+1):
    if dp[i]:
        p.append(i)
        for j in range(1, n // i + 1):
            dp[j * i] = 0

start = 0
end = 0

result = 0
#print(p)
while start < len(p) and end < len(p):
    r = sum(p[start:end + 1])

   # print(r)
    if r == n:
        result += 1
        start += 1
        continue
    elif r > n:
        start += 1
    else:
        end += 1
print(result)
