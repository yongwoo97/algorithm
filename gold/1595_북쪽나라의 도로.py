import sys

input = sys.stdin.readline
graph = {}
line = input().rstrip()

while line:
    a, b, c = map(int, line.split())

    if a in graph:
        graph[a].append([b, c])
    else:
        graph[a] = []
        graph[a].append([b, c])

    if b in graph:
        graph[b].append([a, c])
    else:
        graph[b] = []
        graph[b].append([a, c])

    line = input().replace("\n", "")
#print(graph)

from collections import deque
maxx = 0
def bfs(start):
    global graph, maxx

    q = deque()
    q.append([start, 0])
    visited = [0] * len(graph)
    visited[start-1] = 1
    while q:
        x, y = q.popleft()
        for next, wei in graph[x]:
            if visited[next-1] == 0:
                q.append([next, wei + y])
                visited[next-1] = 1
                maxx = max(maxx, y + wei)

for s in graph:
    bfs(s)
print(maxx)