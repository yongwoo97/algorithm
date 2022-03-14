import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
result = [0] * (n+1)
def dfs(k):
    global visited, graph
    if visited[k]:
        return

    visited[k] = True
    for i in graph[k]:
        if not visited[i]:
            result[i] = k
            dfs(i)
dfs(1)
for k in result[2:]:
    print(k)





