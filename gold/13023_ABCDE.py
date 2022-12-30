import sys
n, m = map(int, input().split())
visited = [0] * (n)
graph = {i:[] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, count):
    global visited, n, m, graph

    if count >= 4:
        print(1)
        exit()
        return 1

    visited[x] = 1

    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, count + 1)
            visited[i] = 0

    visited[x] = 0

    return 0


for i in range( n):
    result = dfs(i, 0)

print(0)