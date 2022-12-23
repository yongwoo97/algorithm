import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
data = [0] + list(map(int, input().split()))

graph = {i:[] for i in range(1, n+1)}

for _ in range(r):
    a, b, c = map(int, input().split())
    #양방향 도로니까 둘다 저장해주고
    graph[a].append([b, c])
    graph[b].append([a, c])
import heapq

def bfs(start):
    global visited, m

    q = []
    heapq.heappush(q, [0, start])
    dp[start] = 0
    visited[start] = 1

    while q:
        limit, cur = heapq.heappop(q)
        visited[cur ] = 1
        if dp[cur] < limit:
            continue
       # print(limit, cur)
        for next, road in graph[cur]:

            if limit + road <= m and dp[next] > limit + road:

                heapq.heappush(q, [limit + road, next])


maxx = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    dp = [float('inf')] * (n + 1)
    bfs(i)
    summ = 0
    for j in range(1, n+1):
        if visited[j] == 1:
            summ += data[j]
    maxx = max(summ, maxx)
    #print(summ, 'durl')
print(maxx)


