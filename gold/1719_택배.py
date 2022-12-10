import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i:[] for i in range(n)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1].append([c, b-1])
    graph[b-1].append([c, a-1])

#dp = [[[float('inf'), -1] for _ in range(n)] for _ in range(n)]

import heapq

def func(cur, weight):
    global n, m, graph

    q = []
    heapq.heappush(q, [weight, cur])

    dp = [[float('inf'), -1] for _ in range(n)]
    dp[cur][0] = 0
    while q:
        w, c = heapq.heappop(q)
        if dp[c][0] < weight:
            continue

        for i in graph[c]:
            nw, nc = i
           #print(nc, c)
            if dp[nc][0] > dp[c][0] + nw:
                dp[nc][0] = dp[c][0] + nw
                if dp[c][1] == -1:
                    dp[nc][1] = nc
                else:
                    dp[nc][1] = dp[c][1]
                heapq.heappush(q, [nw, nc])


    return dp

result = []
for i in range(n):
    semi = func(i, 0)
    for j in range(n):
        if semi[j][1] == -1:
            print('-', end = ' ')
        else:
            print(semi[j][1] + 1, end = ' ')
    print()
