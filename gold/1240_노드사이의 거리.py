#플로이드 와샬
#다익스트라
#벨만포드


#이건 플로이드인데

import sys
input  = sys.stdin.readline

n, m = map(int, input().split())

node = {i: [] for i in range(1001)}
for _ in range(n-1):
    a, b, c = map(int, input().split())
    node[a].append([b,c])
    node[b].append([a,c])

data =[]
for _ in range(m):
    a, b = map(int, input().split())
    data.append([a, b])


def dfs(e, t, c):
    global node, dist

    if e == t:
        dist = c
        return

    visited[e] = 1
    for k in node[e]:
        i, j = k
        if not visited[i]:
            dfs(i, t, c + j)

for x in data:
    z, y = x
    dist = 0
    visited = [0] * 1001
    dfs(z, y, 0)
    print(dist)
