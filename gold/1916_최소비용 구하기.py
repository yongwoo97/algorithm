#힙큐 다익스트라로 먼저 풀어보자
import sys
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c,b])

start, end = map(int, input().split())

visited = [0] * (n + 1)
q = []
visited[start] = 1
result = [float('inf')] * (n+1)
result[start] = 0
heapq.heappush(q, [result[start], start])

while q:
    dist, cur = heapq.heappop(q)

    if dist > result[cur]:
        continue

    for i in range(len(graph[cur])):
        x, y = graph[cur][i]

        if result[y] > result[cur] + x:
            result[y] = result[cur] + x
            heapq.heappush(q, [x, y])


print(result[end])
