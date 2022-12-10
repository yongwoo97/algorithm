n, m = map(int, input().split())


memo = [-1] * (n+1)
memo[1] = 1
for i in range(2, n+1):
    memo[i] = memo[i-1] * i

result = memo[n] // (memo[n-m] * memo[m] )
print(result)