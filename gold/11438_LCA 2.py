import sys
sys.setrecursionlimit(100000)
LOG = 21

n = int(input())

def dfs(x, depth):
    global check, dep, graph, parent

    if check[x]:
        return
    check[x] = True
    dep[x] = depth

    for i in graph[x]:
        if check[i]:
            continue
        parent[i][0] = x
        dfs(i, depth + 1)

def lca(a, b):
    global graph, check, dep


    if dep[a] > dep[b]:
        a, b = b, a

    for i in range(LOG-1, -1, -1):
        if dep[b] - dep[a] >= (1 << i):
            b = parent[b][i]

    if a == b:
        return a

    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)
dep = [0] * (n + 1)
parent = [[0] * (LOG+1) for _ in range(n + 1)]

for i in range(n-1):
    first, last = map(int, input().split())
    graph[first].append(last)
    graph[last].append(first)
dfs(1, 0)

for i in range(1, LOG):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

m = int(input())
re = [tuple(map(int, input().split())) for _ in range(m)]

for k in range(m):
    a, b = re[k]
    print(lca(a, b))



