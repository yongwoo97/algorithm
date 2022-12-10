import sys
'''
n = int(input())
data = []
for _ in range(n):
    line = int(input().rstrip())
    data.append(line)

dp = [[0] * n for _ in range(n)]


result = 0
for d in range(n):
    minn = float('inf')
    for i in range(n-d):
        j = i + d
        if i == j:
            dp[i][j] = data[i]
        else:
            dp[i][j] = min([dp[i][k] + dp[k+1][j] for k in range(i, j)])
        if d > 0:
            minn = min(minn, dp[i][j])
  #  print(minn)
    result += minn

print(result)
'''
#dp 사용하면 메모리 초과
#그리디하게 접근하면 틀림
#힙큐로 접근하면 되었네. 왜 이런 풀이를 떠올리는게 쉽지가 않을까?
#.... 분발하자

input = sys.stdin.readline
import heapq
#최소힙이고
q = []
n = int(input())
for _ in range(n):
    line = int(input())
    heapq.heappush(q, line)

result = 0
while len(q) > 1:
    item_1 = heapq.heappop(q)
    item_2 = heapq.heappop(q)

    semi = item_1 + item_2
    result += semi
    heapq.heappush(q, semi)

print(result)


