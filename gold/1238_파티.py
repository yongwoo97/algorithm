import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = {i: [] for i in range(n)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append([c, b-1])

import heapq
def func(start, end):
    dp = [float('inf')] * n
    q = []
    heapq.heappush(q, [0, start])
    dp[start] = 0
    while q:
        weight, cur = heapq.heappop(q)
        #print(cur, next, weight)
        if dp[cur] < weight:
            continue


        for j in graph[cur]:
            wei, next = j
            if dp[next] > dp[cur] + wei:
                dp[next] = dp[cur] + wei
                heapq.heappush(q, j)

    return dp[end]
result = 0
for i in range(n):
    go = func(i, x-1)
    back = func(x-1, i)
    result = max(result, go+back)
print(result)