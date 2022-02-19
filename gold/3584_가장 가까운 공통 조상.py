import sys
sys.setrecursionlimit(100000)
test = int(input())

def dfs(x, depth):
    global graph, check, dep
    if check[x]:
        return

    dep[x] = depth
    check[x] = True

    for k in graph[x]:
        if check[k]:
            continue
        dfs(k, depth + 1)

def lca(a, b):
    global parent, dep
    if a == b:
        return a

    #항상 b가 더 깊도록 유지한다
    if dep[a] > dep[b]:
        a, b = b, a

    while dep[a] != dep[b]:
        b = parent[b]
    #깊이를 맞춰서 출발하는 이유는 따로따로 출발하면 엇갈려서 공통 조상이 어디서 접점이 생기는 지 알 수 없다.
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

for _ in range(test):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    dep = [0 for _ in range(n+1)]
    check = [False for _ in range(n+1)]
    parent = [0] * (n + 1)
    for_root = [0] * (n + 1)

    for _ in range(n-1):
        i, o = map(int, input().split())
        graph[i].append(o)
        graph[o].append(i)
        parent[o] = i
        for_root[o] = 1
        #양방향으로 하는이유는 거슬러 올라가야 하기 때문에
    root = for_root[1:].index(0) + 1

    dfs(root, 0)

    a1, b1 = map(int, input().split())

    print(lca(a1, b1))






