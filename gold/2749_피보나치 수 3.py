n = int(input())
memo = [0] * 1500001
memo[1] = 1


for i in range(2, 1500001):
    memo[i] = (memo[i-1] + memo[i-2]) % 1000000
print(memo[n%1500000])


