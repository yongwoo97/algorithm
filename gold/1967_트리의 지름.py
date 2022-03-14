import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

max_node = 1
max_dist = 0
visited = [0] * (n+1)
def bfs(k):
    global graph, max_node, max_dist, visited
    q = deque()
    q.append((k, 0))

    while q:
        node, di = q.popleft()
        visited[node] = 1

        if max_dist < di:
            max_node = node
            max_dist = di

        for i in graph[node]:
            new_node, distance = i
            if not visited[new_node]:
                q.append((new_node, di + distance))

bfs(1)
visited = [0] * (n+1)
bfs(max_node)
print(max_dist)