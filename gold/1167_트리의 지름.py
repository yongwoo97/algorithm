import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

graph = {i : [] for i in range(1, n+1)}
for _ in range(1, n+1):
    before = list(map(int, input().split()))[:-1]
    k = before[0]
    before = before[1:]
    for i in range(0, len(before), 2):
        graph[k].append((before[i], before[i+1]))

#print(graph)


visited = [0] * (n+1)
max_dist = 0
max_node = 0

def bfs(s):
    global graph, visited, max_node, max_dist

    q = deque()
    q.append((s, 0))

    while q:
        node, cur_dist = q.popleft()
        if cur_dist > max_dist:
            max_dist = cur_dist
            max_node = node

        visited[node] = 1
        for i in graph[node]:
            new_node, distance = i[0], i[1]
            if not visited[new_node]:
                q.append((new_node, cur_dist + distance))

bfs(1)
visited = [0] * (n+1)
bfs(max_node)
print(max_dist)