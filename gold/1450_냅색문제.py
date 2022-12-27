#N개의 물건과 C 용량의 가방을 가지고 있다. 대표적인 냅색 문제 DP로 풀어가자
#가방의 넣는 방법의 수를 구하래
#이렇게 변형이 생기면 못푸는게 나다.
#근본적인 풀이를 가지고 접근해야해
#흠...
#첫번째 제출에서 메모리 초과가 떴다.
#2차원 배열이 아닌 1차원 배열로 운용해보자
import sys
input = sys.stdin.readline
n, c = map(int, input().split())
data = [0] + list(map(int, input().split()))

dp = [1] * (c+1)

#for i in range(0, n+1):
from copy import deepcopy
for i in range(1, n+1):
    ndp = deepcopy(dp)
    wei = data[i]
    for j in range(1, c+1):
        nj = j - wei
        if 0 <= nj < c + 1:
            ndp[j] = dp[j] + dp[nj]
        else:
            ndp[j] = dp[j]
    dp = ndp

print(dp[c])

#아래는 블로그 본 풀이
import sys
from itertools import combinations

input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

# meet in the middle
arr_1 = arr[:n // 2]
arr_2 = arr[n // 2:]

subsum_a = []
subsum_b = []

for i in range(len(arr_1) + 1):
    comb_a = combinations(arr_1, i)

    for comb in comb_a:
        subsum_a.append(sum(comb))

for i in range(len(arr_2) + 1):
    comb_b = combinations(arr_2, i)

    for comb in comb_b:
        subsum_b.append(sum(comb))

subsum_a.sort()
ans = 0

# subsum_a와 subsum_b의 값을 더하는 작업을 이분탐색으로 진행
for element_b in subsum_b:

    # 이미 subsum_b의 값이 c를 넘었다면 작업 X
    if element_b > c:
        continue

    start = 0
    end = len(subsum_a) - 1

    while start <= end:
        mid = (start + end) // 2

        if subsum_a[mid] + element_b > c:
            end = mid - 1

        else:
            start = mid + 1

    ans += end + 1

print(ans)