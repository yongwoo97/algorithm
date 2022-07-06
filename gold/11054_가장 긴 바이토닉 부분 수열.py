#가장 간단한 풀이 완탐으로 풀어보면되지
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

left = [0] * n
right = [0] * n

lm = 0
for i in range(n):
    mmax = 0
    for j in range(i-1, -1, -1):
        if data[j] >= data[i]:
            continue
        mmax = max(left[j] + 1, mmax)
    left[i] = mmax

for i in range(n-1, -1, -1):
    mmax = 0
    for j in range(i+1, n):
        if data[j] >= data[i]:
            continue
        mmax = max(right[j] + 1, mmax)
    right[i] = mmax


for i in range(n):
    right[i] += left[i]
print(max(right) + 1)
