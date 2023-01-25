import sys
n, m = map(int, input().split())
w = float(input())
graph = {i:[] for i in range(1, n+1)}
import math
data = []
road = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append([y, 0])
    graph[y].append([x, 0])
for i in range(n):
    for j in range(i+1, n):
        x1, y1 = data[i]
        x2, y2 = data[j]
        wei = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
        if wei <= w:
            graph[i+1].append([j+1, wei])
            graph[j+1].append([i+1, wei])

#일단 그래프
#print(graph)

import heapq

def dkjistra(start):
    global graph

    dp = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q, [0, start])
    dp[start] = 0

    while q:
        wei, cur = heapq.heappop(q)
        if dp[cur] < wei:
            continue

        for next, nwei in graph[cur]:
            if dp[next] > dp[cur] + nwei:
                dp[next] = dp[cur] + nwei
                heapq.heappush(q, [nwei, next])

    return dp

r = dkjistra(1)
#print(r)
print(math.floor(r[n] * 1000))
