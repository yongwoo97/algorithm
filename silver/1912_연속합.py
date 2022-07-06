#2차원 dp로 풀어봅시다. 1번 풀이.
#2번 풀이는 1차원 dp 이고 최대값에서 최소값을 빼면되지 않을까?
'''
#2번 풀이 n2은 시간초과가 뜨네
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

mem = 0
result = [0] * n

for i in range(n):
    mem += data[i]
    result[i] = mem


mmax = 0
for i in range(n):
    for j in range(i-1, -1, -1):
        semi = result[i] - result[j]
        if semi > mmax:
            mmax = semi
print(mmax)
'''
#1번 풀이
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

mem = 0
result = [0] * n

for i in range(n):
    mem += data[i]
    result[i] = mem

mmax = float('-inf')
dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i > j:
            continue
        elif i == j:
            dp[i][j] = data[i]
        else:
            dp[i][j] = result[j] - result[i]

        if dp[i][j] > mmax:
            mmax = dp[i][j]

print(mmax)

#최종 풀이
n = int(input())

arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])

print(max(dp))